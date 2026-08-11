"""Page complementaire -- A propos, methodologie, qualite des donnees et limites."""

from __future__ import annotations

import streamlit as st

from components.header import render_header
from config.settings import (
    AUTHOR_BIO,
    AUTHOR_EMAIL,
    AUTHOR_GITHUB,
    AUTHOR_LINKEDIN,
    AUTHOR_NAME,
    AUTHOR_PHONE,
    AUTHOR_TITLE,
    AUTHOR_WHATSAPP,
    DATA_DICTIONARY_CSV,
)


def render(data_dictionary) -> None:
    render_header(
        page_title="A propos et methodologie",
        page_subtitle="Sources, qualite des donnees, limites et contact",
    )

    st.markdown("### Sources")
    st.markdown(
        "- Indice de risque d'inondation (FRI) par canton -- Togo AI Lab, fevrier 2026 (couverture nationale, 388 cantons).\n"
        "- Sous-projets d'hydraulique rurale du programme COSO, finance par la Banque mondiale.\n"
        "- Points de forages et chateaux d'eau geres par la Togolaise des Eaux (TdE).\n"
        "- Recensement demographique 2010 (donnee de contexte, non utilisee pour le calcul du WUI)."
    )

    st.markdown("### Qualite des donnees")
    with st.expander("Consulter le data dictionary consolide"):
        st.dataframe(data_dictionary, width="stretch", hide_index=True)

    

    st.markdown("### A propos de l'application")
    st.markdown(
        f"""
        **{AUTHOR_NAME}**
        {AUTHOR_TITLE}

        {AUTHOR_BIO}

        Email : [{AUTHOR_EMAIL}](mailto:{AUTHOR_EMAIL})
        
        LinkedIn : [{AUTHOR_LINKEDIN}]({AUTHOR_LINKEDIN})
        """
    )
