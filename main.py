import time
import os
from collections import deque
import matplotlib.pyplot as plt

# Config
green_light_duration = 5  # seconds
num_cycles = 1
directions = deque(["North", "South", "East", "West"])

# Track timeline
timeline = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_traffic_light(active, queue, seconds_left, ambulance=None):
    print("=== Traffic Light Simulation ===\n")
    print(f"Current Queue Order: {list(queue)}\n")
    if ambulance:
        print(f"🚨 Ambulance is coming from {ambulance}! Prioritizing...\n")
    for direction in directions:
        if direction == active:
            print(f"[{direction}] - 🟢 GREEN ({seconds_left} seconds left)")
        else:
            print(f"[{direction}] - 🔴 RED")

def round_robin_simulation():
    current_time = 0
    rr_queue = directions.copy()
    
    for cycle in range(num_cycles * len(directions)):
        current_direction = rr_queue[0]

        timeline.append((current_direction, current_time, green_light_duration))

        for seconds_left in range(green_light_duration, 0, -1):
            clear_screen()
            print(f"Cycle {cycle + 1}, {current_direction}'s turn")
            show_traffic_light(current_direction, rr_queue, seconds_left)
            time.sleep(1)

        current_time += green_light_duration
        rr_queue.rotate(-1)

    clear_screen()
    print("=== Round Robin Simulation Complete ===\n")

def srt_simulation():
    # Ask user for ambulance direction
    print("\nAmbulance Incoming Simulation")
    print("Choose the direction the ambulance is coming from:")
    print("1. North")
    print("2. South")
    print("3. East")
    print("4. West")
    direction_map = {'1': "North", '2': "South", '3': "East", '4': "West"}

    ambulance_choice = input("Enter the number (1-4): ").strip()
    ambulance_direction = direction_map.get(ambulance_choice, None)

    if not ambulance_direction:
        print("Invalid direction selected. Returning to menu.")
        return

    current_time = 0
    srt_queue = directions.copy()

    ambulance_time = 6  # Seconds into simulation when ambulance appears
    ambulance_handled = False
    ambulance_cycles_needed = 2
    ambulance_cycles_given = 0
    ambulance_announcement_done = False
    post_ambulance_final_cycle = False
    final_queue = deque()

    time_step = 1  # Simulate time in 1-second steps

    while True:
        # Decide which direction gets green light
        if not ambulance_handled and current_time >= ambulance_time:
            ambulance_handled = True
            ambulance_cycles_given = 0
            current_direction = ambulance_direction

            # Announce only once
            if not ambulance_announcement_done:
                clear_screen()
                print(f"\n🚨 Ambulance detected from {ambulance_direction}! Preempting to prioritize.\n")
                ambulance_announcement_done = True
                time.sleep(2)
        elif ambulance_handled and ambulance_cycles_given < ambulance_cycles_needed:
            current_direction = ambulance_direction
        elif ambulance_handled and not post_ambulance_final_cycle:
            # After ambulance is done, prepare a final full cycle for remaining directions
            final_queue = deque(d for d in directions if d != ambulance_direction)
            post_ambulance_final_cycle = True

        elif post_ambulance_final_cycle:
            if final_queue:
                current_direction = final_queue.popleft()
            else:
                break  # Final cycle done → end simulation
        else:
            current_direction = srt_queue[0]

        # Show priority queue (for UI display only)
        if ambulance_handled and ambulance_cycles_given < ambulance_cycles_needed:
            display_queue = deque([ambulance_direction]) + deque(d for d in srt_queue if d != ambulance_direction)
        elif post_ambulance_final_cycle:
            display_queue = final_queue.copy()
        else:
            display_queue = srt_queue

        # Show traffic light and simulate duration
        for seconds_left in range(green_light_duration, 0, -1):
            clear_screen()
            show_traffic_light(current_direction, display_queue, seconds_left,
                               ambulance_direction if ambulance_handled and ambulance_cycles_given < ambulance_cycles_needed else None)
            timeline.append((current_direction, current_time, 1))
            current_time += 1
            time.sleep(time_step)

        # Queue control
        if ambulance_handled and ambulance_cycles_given < ambulance_cycles_needed:
            ambulance_cycles_given += 1
        elif not post_ambulance_final_cycle and not ambulance_handled:
            srt_queue.rotate(-1)

    clear_screen()
    print("=== SRT (Ambulance Priority) Simulation Complete ===\n")


def show_menu():
    print("=== Traffic Light Scheduler ===")
    print("Choose Scheduling Algorithm:")
    print("1. Round Robin")
    print("2. SRT (with Ambulance Priority)")
    choice = input("Enter your choice (1 or 2): ")
    return choice.strip()

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            round_robin_simulation()
        elif choice == '2':
            srt_simulation()
        else:
            print("Invalid choice. Please select 1 or 2.\n")
        
        again = input("Do you want to run another simulation? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
