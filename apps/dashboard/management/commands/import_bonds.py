# yourapp/management/commands/import_bonds_data.py

import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.dashboard.models import Dataname, DataValue  # Replace "yourapp" with your actual app name

class Command(BaseCommand):
    help = 'Import Indonesia 10Y Bonds data from the provided API'

    def handle(self, *args, **options):
        url = "https://markets.tradingeconomics.com/chart/gidn10yr:gov?interval=1d&span=1y&securify=new&url=/indonesia/government-bond-yield&AUTH=%2B9me8Xo4n3nb7tygYu6eu%2BJATytAOBGUVd7ZuHeu75wFukp%2Bl4ivUABaPno6D4gwBugPPPYkYB4kyfZzUmN5gA%3D%3D&ohlc=0"

        response = requests.get(url)
        data = response.json()

        series_data = data.get("series", [])
        if not series_data:
            self.stdout.write(self.style.ERROR("No series data found."))
            return

        bonds_series = series_data[0].get("data", [])
        if not bonds_series:
            self.stdout.write(self.style.ERROR("No Indonesia 10Y Bonds series data found."))
            return

        # Create Dataname instance for Indonesia 10Y Bonds
        dataname, created = Dataname.objects.get_or_create(
            title="Indonesia 10Y Bonds",
            defaults={
                'periode': None,  # You might want to set this to a specific Option instance
                'source': url,
                'keterangan': "Indonesia 10Y Bonds Yield data",
            }
        )

        # Create DataValue instances for new dates
        for entry in bonds_series:
            date_str = entry.get("date")
            value = entry.get("y")

            if date_str and value:
                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

                # Check if DataValue with the same title and date already exists
                if not DataValue.objects.filter(title=dataname, date=date).exists():
                    DataValue.objects.create(title=dataname, date=date, value=value)

        self.stdout.write(self.style.SUCCESS("Data from the Indonesia 10Y Bonds API has been successfully imported."))
