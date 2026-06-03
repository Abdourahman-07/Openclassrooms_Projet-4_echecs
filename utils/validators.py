"""Fonctions de validation pour les saisies utilisateur."""
from datetime import datetime


def ask_date(view, prompt):
    """Demande une date au format YYYY-MM-DD et la valide.

    Tant que l'utilisateur n'entre pas une date valide au format
    AAAA-MM-JJ, un message d'erreur est affiché et la saisie est redemandée.
    """
    while True:
        date_str = view.get_input(prompt)
        try:
            # Vérifie format + validité
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            view.display_error(
                "Date invalide. Utilisez le format YYYY-MM-DD"
            )
            continue
        return date_str