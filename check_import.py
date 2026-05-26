try:
    import importlib
    importlib.import_module("hermes_trading.run")
    print("IMPORT_OK")
except Exception as e:
    import traceback
    print("IMPORT_ERROR:", repr(e))
    traceback.print_exc()
