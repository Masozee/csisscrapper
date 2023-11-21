# yourapp/management/commands/import_nickel_data.py

import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.dashboard.models import Dataname, DataValue  # Replace "yourapp" with your actual app name


class Command(BaseCommand):
    help = 'Import Nickel data from the provided API'

    def handle(self, *args, **options):
        url = "https://markets.tradingeconomics.com/chart/ln1:com?interval=1d&span=1y&securify=new&url=/commodity/nickel&AUTH=ismMqWix7RTZXpUuidGkbvLDuLGd5RDTMEUOanZVgX91UwbZ72rfkW73ZT%2BozOt3&ohlc=0"

        response = requests.get(url)
        data = response.json()

        series_data = data.get("series", [])
        if not series_data:
            self.stdout.write(self.style.ERROR("No series data found."))
            return

        nickel_series = series_data[0].get("data", [])
        if not nickel_series:
            self.stdout.write(self.style.ERROR("No Nickel series data found."))
            return

        # Create Dataname instance for Nickel
        dataname, created = Dataname.objects.get_or_create(
            title="Nickel",
            defaults={
                'periode': None,  # You might want to set this to a specific Option instance
                'source': url,
                'keterangan': "Nickel commodity data",
            }
        )

        # Create DataValue instances for new dates
        for entry in nickel_series:
            date_str = entry.get("date")
            value = entry.get("y")

            if date_str and value:
                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

                # Check if DataValue with the same title and date already exists
                if not DataValue.objects.filter(title=dataname, date=date).exists():
                    DataValue.objects.create(title=dataname, date=date, value=value)

        self.stdout.write(self.style.SUCCESS("Data from the Nickel API has been successfully imported."))
