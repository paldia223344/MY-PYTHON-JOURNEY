try:
    print("Hello world!", end=" ")
except TypeError:
    print("Invalid Datatype", end=" ")
except ValueError:
    print("Invalid Value", end=" ")
except Exception:
    print("Error occurred", end=" ")
finally:
    print("Last block")