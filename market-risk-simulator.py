import random
import time


def run_simulation():
    print("=" * 60)
    print("      AI SECTOR MARKET SIMULATOR (VER 1.0)      ")
    print("=" * 60)

    # Getting input from user (Whole numbers only)
    user_input = input(">> ENTER STARTING CAPITAL ($): ")
    money = int(user_input)

    # Target: 2x Return (Investment Goal)
    target = int(money * 2)

    year = 1
    max_years = 5

    print("-" * 60)
    print(f"STARTING CAPITAL : ${money}")
    print(f"TARGET GOAL      : ${target}")
    print(f"DURATION         : {max_years} Years")
    print("-" * 60)

    while money > 0 and year <= max_years:

        print(f"\n[ YEAR {year} OF {max_years} ]")
        print(f"CURRENT BALANCE: ${money}")
        print("-" * 60)

        # 1: Good Market, 2: Bad Market, 3: Uncertain
        market_status = random.randint(1, 3)

        print("MARKET NEWS:")
        if market_status == 1:
            print(">> NEWS: Tech Sector Rally. Prices are UP.")
        elif market_status == 2:
            print(">> NEWS: New Regulations Announced. Prices are DOWN.")
        else:
            print(">> NEWS: Market Volatility High. Trend Uncertain.")

        print("-" * 60)

        print("CHOOSE STRATEGY:")
        print(" [1] AGGRESSIVE (Buy AI Stocks)")
        print(" [2] DEFENSIVE  (Keep Cash/Bonds)")

        choice = input("\n>> ENTER CHOICE (1 or 2): ")

        print("\nPROCESSING ORDER...")
        time.sleep(1)

        change = 0

        # Option 1: Aggressive (High Risk)
        if choice == "1":
            if market_status == 1:
                # Market is Good + Aggressive = High Return
                change = money * 0.50
                print(f">> RESULT: MARKET RALLY. HIGH RETURN. +${int(change)}")
            elif market_status == 2:
                # Market is Bad + Aggressive = High Loss
                change = -(money * 0.40)
                print(f">> RESULT: MARKET CRASH. STOP LOSS HIT. -${int(abs(change))}")
            else:
                # Uncertain Market (50% Chance)
                luck = random.randint(0, 1)
                if luck == 1:
                    change = money * 0.20
                    print(f">> RESULT: RISK PAID OFF. GAIN. +${int(change)}")
                else:
                    change = -(money * 0.20)
                    print(f">> RESULT: VOLATILITY LOSS. -${int(abs(change))}")

        # Option 2: Defensive (Safe Mode)
        elif choice == "2":
            if market_status == 2:
                # Market is Bad + Defensive = Capital Preservation
                change = 0
                print(f">> RESULT: STRATEGY SUCCESSFUL. CAPITAL PRESERVED.")
            else:
                # Market is Good + Defensive = Opportunity Cost
                change = money * 0.05
                print(f">> RESULT: LOW YIELD RETURN. +${int(change)}")

        else:
            print(">> ERROR: INVALID INPUT.")
            change = 0

        money += int(change)

        # Check Win Condition
        if money >= target:
            print("\n" + "=" * 60)
            print(" TARGET REACHED. ROI ACHIEVED.")
            print(f" FINAL BALANCE: ${money}")
            print("=" * 60)
            return

        year += 1

    # End of Loop
    print("\n" + "=" * 60)
    print(" SIMULATION ENDED")
    print("-" * 60)

    if money >= int(user_input):
        print(f" FINAL BALANCE: ${money}")
        print(" STATUS: PROFITABLE PORTFOLIO")
    else:
        print(f" FINAL BALANCE: ${money}")
        print(" STATUS: LOSS")
    print("=" * 60)


run_simulation()