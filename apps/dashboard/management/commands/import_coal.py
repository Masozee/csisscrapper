# yourapp/management/commands/import_coal_data.py

import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.dashboard.models import Dataname, DataValue  # Replace "yourapp" with your actual app name

class Command(BaseCommand):
    help = 'Import Coal data from the provided API'

    def handle(self, *args, **options):
        url = "https://markets.tradingeconomics.com/chart/xal1:com?interval=1d&span=1y&securify=new&url=/commodity/coal&AUTH=7SrvbwMLGi31l0gI9oYpNZeQU%2FhaVADrqgQ1hRjhhLo2DpwSPbCqlolvbil3wSQw&ohlc=0"

        response = requests.get(url)
        data = response.json()

        series_data = data.get("series", [])
        if not series_data:
            self.stdout.write(self.style.ERROR("No series data found."))
            return

        coal_series = series_data[0].get("data", [])
        if not coal_series:
            self.stdout.write(self.style.ERROR("No Coal series data found."))
            return

        # Create Dataname instance for Coal
        dataname, created = Dataname.objects.get_or_create(
            title="Coal",
            defaults={
                'periode': None,  # You might want to set this to a specific Option instance
                'source': url,
                'keterangan': "Coal commodity data",
            }
        )

        # Create DataValue instances for new dates
        for entry in coal_series:
            date_str = entry.get("date")
            value = entry.get("y")

            if date_str and value:
                date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

                # Check if DataValue with the same title and date already exists
                if not DataValue.objects.filter(title=dataname, date=date).exists():
                    DataValue.objects.create(title=dataname, date=date, value=value)

        self.stdout.write(self.style.SUCCESS("Data from the Coal API has been successfully imported."))
