from libs.openexchange import OpenExchangeClient

APP_ID = '2a644459018a4b98b8a45f4283840222'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gdb_amount = client.convert(usd_amount, "USD", "GBP")

print(f"USD{usd_amount} is GBP{gdb_amount:.2f}")


