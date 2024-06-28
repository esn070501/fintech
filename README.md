# Introduction
EventEats aims to enhance the event experience by reducing wait times for food and beverages through a mobile app that allows attendees to request and fulfill orders within the event venue. This repository includes files that simulate the backend of the final product and test the user interface.

# Files
This repository contains the following key files:

fake_data.ipynb: A Jupyter notebook that creates synthetic data to simulate the backend of the final product. It is used to determine a value for alpha in the dynamic pricing calculation.
user_interface.py: A Python script that handles the user interface for placing and fulfilling orders.
fake_data.ipynb
The fake_data.ipynb notebook includes the following sections:

Data Generation: Creates synthetic data to simulate event scenarios, including user behavior and order placements.
Alpha Calculation: Analyzes the synthetic data to determine the optimal value for alpha in the dynamic pricing algorithm. Alpha helps adjust the pricing premium based on real-time demand.
user_interface.py

The user_interface.py script includes:

User Registration: Functions for new users to register and existing users to log in.
Order Placement: Allows users to place food and beverage orders, specifying their seating area.
Order Fulfillment: Enables nearby attendees to accept and fulfill orders.
Payment Processing: Handles secure payment transactions for completed orders.
