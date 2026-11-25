import yfinance as yf

data = yf.download("AAPL", period="1mo", auto_adjust=True)

# Flatten MultiIndex columns if present
if hasattr(data.columns, "nlevels") and data.columns.nlevels > 1:
    data.columns = data.columns.get_level_values(0)

# Move Date index into a column and format cleanly
records_df = data.reset_index()
records_df["Date"] = records_df["Date"].dt.strftime("%Y-%m-%d")

# JSON string (pretty-printed with indent=2)
json_output = records_df.to_json(orient="records", indent=2)
print(json_output)

# Or write directly to a file for a frontend to load
records_df.to_json("aapl_history.json", orient="records", indent=2)