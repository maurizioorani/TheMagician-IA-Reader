
from langchain.prompts import PromptTemplate
import pandas as pd
from langchain_core.runnables import RunnableParallel, RunnableLambda # Import necessario per LCEL
import random
import streamlit as st
import helpers.help_func as hf



# --- Carica il dataset ---
csv_file_path = 'data/tarocchi.csv'
try:
    # Read CSV file
    df = pd.read_csv(csv_file_path, sep=';', encoding='utf-8')
    print(f"Dataset CSV caricato con successo da {csv_file_path}. Numero di righe: {len(df)}")
    
    # Clean and normalize column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Debug: Show column details
    print("\nDettagli colonne dopo pulizia:")
    for col in df.columns:
        print(f"Colonna: '{col}' (lunghezza: {len(col)})")
    
    # Define required columns (in lowercase)
    required_columns = ['carte', 'dritto', 'rovescio']
    
    # Verify all required columns are present
    available_columns = set(df.columns)
    missing_columns = [col for col in required_columns if col not in available_columns]
    
    if missing_columns:
        raise ValueError(
            f"Colonne mancanti nel CSV: {', '.join(missing_columns)}\n"
            f"Colonne disponibili: {', '.join(available_columns)}"
        )
    
    # Create card meanings dictionary with cleaned data
    card_meanings = {}
    for _, row in df.iterrows():
        card_name = row['carte'].strip()
        card_meanings[card_name] = {
            'dritto': str(row['dritto']).strip() if pd.notna(row['dritto']) else '',
            'rovescio': str(row['rovescio']).strip() if pd.notna(row['rovescio']) else ''
        }
    
    print(f"\nBase di conoscenza creata con {len(card_meanings)} carte.")
    
except FileNotFoundError:
    print(f"Errore: File CSV non trovato: {csv_file_path}")
    raise
except ValueError as e:
    print(f"Errore di validazione: {str(e)}")
    raise
except Exception as e:
    print(f"Errore imprevisto: {str(e)}")
    raise



# --- Definisci il Prompt Template ---
prompt_analisi = PromptTemplate.from_template("""
Analizza le seguenti carte dei tarocchi, basandoti sui significati forniti (considerando anche se sono al rovescio):
{card_details}
Quando parli della persona che ha estratto le carte, usa "il consultante". Usa sempre il "tu" per riferirti al consultante.
Fornisci un'analisi dettagliata del significato di *ciascuna* carta (dritta o rovesciata).
Poi, offri un'interpretazione generale delle carte *nel loro insieme*, legandola al contesto: {contesto}, e offri dei consigli per migliorare la situazione.
Sii sempre professionale ed empatico nel fornire le tue risposte.
""")
print("\nPrompt Template 'prompt_analisi' definito.")

# --- Crea la Catena LangChain ---
analizzatore = (
    RunnableParallel(
        carte=lambda x: x['carte'],
        contesto=lambda x: x['contesto']
    )
    | (lambda x: hf.prepare_prompt_input(x, card_meanings))
    | prompt_analisi
    | hf.llm
)


# --- Frontend Streamlit ---
st.set_page_config(
    page_title="🔮 Lettura Interattiva dei Tarocchi",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("🔮 Lettura Interattiva dei Tarocchi")
st.markdown("Benvenuto nel tuo consulto di tarocchi personalizzato!")
st.markdown("---")

numero_carte = st.selectbox("🃏 Seleziona il numero di carte per la tua stesa (3 per una risposta più puntuale, 7 per una visione più generale)", [3, 5, 7])
contesto_domanda = st.text_area("✍️ Inserisci qui il tuo contesto o la tua domanda. Puoi parlare in linguaggio naturale", height=100)

if st.button("✨ Illumina il tuo cammino: Estrai e Analizza le Carte"):
    if not contesto_domanda:
        st.warning("Per una lettura più precisa, inserisci il tuo contesto o domanda.")
    else:
        try:
            nomi_carte_nel_dataset = df['carte'].unique().tolist()
            lista_di_carte_estratte = hf.genera_estrazione_casuale(numero_carte, nomi_carte_nel_dataset)
            st.subheader("✨ Le Carte Rivelate:")
            st.markdown("---")

            cols = st.columns(len(lista_di_carte_estratte))
            for i, carta_info in enumerate(lista_di_carte_estratte):
                with cols[i]:
                    nome_carta = carta_info['nome'].replace(" ", "_")
                    immagine_path = f"images/{nome_carta}.jpg"
                    rovesciata_label = "(R)" if 'rovesciata' in carta_info else ""
                    caption = f"{carta_info['nome']} {rovesciata_label}"

                    try:
                        st.image(immagine_path, caption=caption, width=150)
                    except FileNotFoundError:
                        st.info(f"Simbolo: {carta_info['nome']} {rovesciata_label}")

            st.markdown("---")
            with st.spinner("🔮 Svelando i significati..."):
                risultato_analisi = analizzatore.invoke({"carte": lista_di_carte_estratte, "contesto": contesto_domanda})
                st.subheader("📜 L'Interpretazione:")
                st.write(risultato_analisi.content)

        except Exception as e:
            st.error(f"Si è verificato un errore: {e}")
            st.error(f"Dettagli dell'errore: {e}")

st.markdown("---")
st.info("Ricorda, le carte offrono spunti e riflessioni, il tuo futuro è nelle tue mani.")