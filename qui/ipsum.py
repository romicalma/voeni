try:
    # Some long-running operation or loop
    while True:
        print("Running...")
except KeyboardInterrupt:
    pass  # Handle keyboard interrupt by doing nothing
