"""Fonctions de validation pour les saisies utilisateur."""
from datetime import datetime


def ask_date(view, prompt):
    """Demande une date au format YYYY-MM-DD et la valide.

    Tant que l'utilisateur n'entre pas une date valide au format
    AAAA-MM-JJ, un message d'erreur est affiché et la saisie est redemandée.

    Args:
        view: Objet vue (interface) fournissant les méthodes `get_input`
              et `display_error`.
        prompt: Message affiché à l'utilisateur pour demander la date.

    Returns:
        str: La date saisie par l'utilisateur, validée au format YYYY-MM-DD.
    """
    while True:
        # Récupère la saisie utilisateur via la vue
        date_str = view.get_input(prompt)
        try:
            # Vérifie format + validité de la date (lève ValueError si invalide)
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            # Affiche un message d'erreur et redemande la saisie
            view.display_error(
                "Date invalide. Utilisez le format YYYY-MM-DD"
            )
            continue
        # Si aucune exception n'est levée, la date est valide
        return date_str
