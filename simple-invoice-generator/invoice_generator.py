import json

def load_invoice(path):
    with open(path, "r") as f:
        return json.load(f)

def format_invoice(data):
    client = data.get("client", {})
    invoice = data.get("invoice", {})
    items = data.get("items", [])

    lines = []
    lines.append("INVOICE")
    lines.append("-------\n")

    lines.append(f"Client: {client.get('name', '')}")
    address = f"{client.get('address', '')}, {client.get('city', '')}".strip(", ")
    lines.append(f"Address: {address}")
    lines.append(f"Email: {client.get('email', '')}\n")

    lines.append(f"Invoice Number: {invoice.get('invoice_number', '')}")
    lines.append(f"Date: {invoice.get('date', '')}\n")

    lines.append("Items:")
    subtotal = 0

    for item in items:
        desc = item.get("description", "")
        amt = item.get("amount", 0)
        subtotal += amt
        lines.append(f"  • {desc} .......... ${amt}")

    lines.append(f"\nSubtotal: ${subtotal}")
    lines.append(f"Total: ${subtotal}")

    return "\n".join(lines)

def main():
    path = input("Enter path to invoice JSON file: ").strip()
    data = load_invoice(path)
    output = format_invoice(data)
    print("\n" + output)

if __name__ == "__main__":
    main()