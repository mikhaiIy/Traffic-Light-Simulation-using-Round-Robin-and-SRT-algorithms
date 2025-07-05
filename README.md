# 🚦 Traffic Light Scheduling Simulation using Round Robin and SRT

This project simulates a traffic light control system using two scheduling algorithms: **Round Robin** and **Shortest Remaining Time (SRT)**. Inspired by CPU scheduling in operating systems, the simulation demonstrates how time-based and priority-based traffic control mechanisms can be used to manage a four-way intersection.

The program is written in **Python** and runs in the terminal with dynamic visual output. It allows users to choose between a balanced traffic scenario (Round Robin) or a dynamic emergency scenario (SRT with ambulance priority).

---

## 📌 Features

- ✅ **Round Robin Scheduling** – Each direction gets equal green light time in a cyclic order.
- 🚨 **SRT with Ambulance Preemption** – Traffic flow dynamically prioritizes the direction with an ambulance.
- 📊 **Real-Time Output** – Terminal-based simulation shows green/red states per second.
- 📈 **Gantt Chart Ready** – Timeline can be extended for plotting and analysis (using `matplotlib`).
- 🧠 **Educational Use** – Great for learning scheduling logic and simulation development.

---

## 🧪 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mikhaiIy/Traffic-Light-Simulation-using-Round-Robin-and-SRT-algorithms.git

   cd traffic-light-scheduling

2. **📦 requirements.txt**
Use `pip install -r requirements.txt` to install dependencies.

3. **Run the program**:
   ```bash
   python main.py

4. **Choose your simulation type when prompted:**
- Option 1 – Round Robin
- Option 2 – SRT with ambulance priority

## 📂 File Structure
   ```bash
    traffic-light-scheduling/
├── main.py              # Main simulation script
├── README.md            # Project documentation (this file)
├── requirements.txt     # Required Python packages
└── .gitignore           


