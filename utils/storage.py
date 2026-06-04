import json
import os
from models.player import Player
from models.tournament import Tournament


class Storage:
    """Classe gérant la sauvegarde et le chargement des données.

    Les joueurs sont stockés dans un seul fichier JSON, tandis que
    chaque tournoi est sauvegardé dans un fichier séparé dans un
    répertoire dédié.
    """

    PLAYERS_FILE = "data/players.json"
    TOURNAMENTS_DIR = "data/tournaments"

    @classmethod
    def ensure_data_directories(cls):
        """Crée les répertoires de données s'ils n'existent pas."""
        os.makedirs(os.path.dirname(cls.PLAYERS_FILE), exist_ok=True)
        os.makedirs(cls.TOURNAMENTS_DIR, exist_ok=True)

    # ---------- Gestion des joueurs ----------

    @classmethod
    def load_players(cls):
        """Charge tous les joueurs depuis le fichier JSON.

        Returns:
            dict[str, Player]: Dictionnaire {player_id: Player}.
        """
        cls.ensure_data_directories()
        if not os.path.exists(cls.PLAYERS_FILE):
            return {}

        with open(cls.PLAYERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {pid: Player.from_dict(pdata) for pid, pdata in data.items()}

    @classmethod
    def save_players(cls, players):
        """Sauvegarde tous les joueurs dans le fichier JSON.

        Args:
            players: Dictionnaire {player_id: Player}.
        """
        cls.ensure_data_directories()
        data = {pid: player.to_dict() for pid, player in players.items()}
        with open(cls.PLAYERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # ---------- Gestion des tournois ----------

    @classmethod
    def load_tournaments(cls):
        """Charge tous les tournois depuis les fichiers JSON.

        Returns:
            dict[str, Tournament]: Dictionnaire {nom: Tournament}.
        """
        cls.ensure_data_directories()
        tournaments = {}

        if not os.path.exists(cls.TOURNAMENTS_DIR):
            return tournaments

        for filename in os.listdir(cls.TOURNAMENTS_DIR):
            if filename.endswith(".json"):
                filepath = os.path.join(cls.TOURNAMENTS_DIR, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                tournament = Tournament.from_dict(data)
                tournaments[tournament.name] = tournament

        return tournaments

    @classmethod
    def save_tournament(cls, tournament):
        """Sauvegarde un tournoi dans un fichier JSON.

        Le nom du fichier est basé sur le nom du tournoi, avec les espaces
        remplacés par des underscores.

        Args:
            tournament: Instance de Tournament à sauvegarder.
        """
        cls.ensure_data_directories()
        filename = f"{tournament.name.replace(' ', '_')}.json"
        filepath = os.path.join(cls.TOURNAMENTS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tournament.to_dict(), f, indent=2, ensure_ascii=False)
