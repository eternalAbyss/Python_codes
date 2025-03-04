transaction_id = "Something"
txn_id = lambda x: x if x is not None else transaction_id
print(txn_id("info"))  # Something