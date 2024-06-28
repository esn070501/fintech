import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QHBoxLayout, QMessageBox, QScrollArea
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QLinearGradient, QPainter, QBrush, QPen, QFontMetrics
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QStyleOptionButton, QStyle, QFrame
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QTimeEdit
# import QGridLayout
from PyQt5.QtWidgets import QGridLayout
import random


################### LOGIN PAGE ###################
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EventEats - Login")
        self.setFixedSize(400, 700)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Logo and company name
        logo_label = QLabel(self)
        pixmap = QPixmap("company_logo.png").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        company_name_label = QLabel("EventEats", self)
        company_name_label.setAlignment(Qt.AlignCenter)
        company_name_label.setFont(QFont('Roboto', 36, QFont.Bold))
        company_name_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Welcome label
        welcome_label = QLabel("Welcome", self)
        welcome_label.setFont(QFont('Roboto', 24, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("color: #34495e; margin-bottom: 30px;")

        # Username and password inputs
        input_style = """
            QLineEdit {
                padding: 10px;
                background-color: rgba(255, 255, 255, 0.8);
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
        """

        self.username_entry = QLineEdit(self)
        self.username_entry.setPlaceholderText("Username")
        self.username_entry.setStyleSheet(input_style)

        self.password_entry = QLineEdit(self)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setStyleSheet(input_style)

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setFont(QFont('Roboto', 16))
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.login_button.clicked.connect(self.login)

        # Create Account button
        self.create_account_button = QPushButton("Create Account", self)
        self.create_account_button.setFont(QFont('Roboto', 14))
        self.create_account_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.create_account_button.clicked.connect(self.create_account)

        # Forgot password link
        self.forgot_password = QLabel("<a href='#'>Forgot password?</a>", self)
        self.forgot_password.setFont(QFont('Roboto', 12))
        self.forgot_password.setStyleSheet("color: #3498db; margin-top: 10px;")
        self.forgot_password.setAlignment(Qt.AlignCenter)
        self.forgot_password.setOpenExternalLinks(False)
        self.forgot_password.linkActivated.connect(self.forgot_password_clicked)

        # Adding widgets to layout
        main_layout.addWidget(logo_label)
        main_layout.addWidget(company_name_label)
        main_layout.addWidget(welcome_label)
        main_layout.addWidget(self.username_entry)
        main_layout.addWidget(self.password_entry)
        main_layout.addWidget(self.login_button)
        main_layout.addWidget(self.create_account_button)
        main_layout.addWidget(self.forgot_password)
        main_layout.addStretch(1)

        # Set layout
        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        print(f"Username: {username}")
        print(f"Password: {password}")

        # Open the EventsPage
        self.events_page = EventsPage()
        self.events_page.show()
        self.close()

    def create_account(self):
        print("Create account clicked")
        QMessageBox.information(self, 'Create Account', "Create account clicked")

    def forgot_password_clicked(self):
        print("Forgot password clicked")
        QMessageBox.information(self, 'Forgot Password', "Forgot password clicked")



################### EVENTS PAGE ###################
class EventsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EventEats - Current Events")
        self.setFixedSize(400, 700)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Add some spacing at the top
        main_layout.addSpacing(10)

        title_label = QLabel("Current Events", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            color: #2c3e50;
            padding: 5px 15px;
        """)

        main_layout.addWidget(title_label)

        # Reduced spacing between title and events
        main_layout.addSpacing(10)

        # Reduced spacing between title and events
        main_layout.addSpacing(10)

        # Create a container for the events
        events_container = QWidget()
        events_container.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 15px;
        """)
        events_layout = QVBoxLayout(events_container)

        events = [
            "Kanye West - Release Party",
            "Euro Cup - Germany vs. Portugal",
            "NBA - Lakers vs. Warriors",
            "Beyoncé - Renaissance World Tour",
            "Coldplay - Music of the Spheres World Tour"
        ]

        for event in events:
            event_button = QPushButton(event)
            event_button.setFont(QFont('Roboto', 16))
            event_button.setStyleSheet("""
                QPushButton {
                    background-color: rgba(52, 152, 219, 0.8);
                    color: white;
                    border: none;
                    padding: 15px;
                    border-radius: 10px;
                    margin: 5px 0;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: rgba(41, 128, 185, 0.9);
                }
            """)
            event_button.clicked.connect(lambda checked, e=event: self.select_event(e))
            events_layout.addWidget(event_button)

        main_layout.addWidget(events_container)

        # Add stretching space
        main_layout.addStretch(1)

        # Add Back button
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        back_button.clicked.connect(self.go_back)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def go_back(self):
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()
    
    def select_event(self, event_name):
        self.seating_area_page = SeatingAreaPage(event_name)
        self.seating_area_page.show()
        self.close()

################### SEATING AREA PAGE ###################
class SeatingAreaPage(QWidget):
    def __init__(self, event_name):
        super().__init__()
        self.setWindowTitle(f"EventEats - Seating Areas")
        self.seating_area = None
        self.setFixedSize(400, 700)
        self.event_name = event_name
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(22, 22, 22, 22)

        # Event title
        event_label = self.create_split_title_label()
        
        # Select instruction
        select_label = QLabel("Please Select Your Seating Area")
        select_label.setFont(QFont('Lato', 18))
        select_label.setStyleSheet("color: #7f8c8d; margin-top: 30px; margin-bottom: 25px; font-weight: 300;")
        select_label.setAlignment(Qt.AlignCenter)
        
        main_layout.addWidget(event_label)
        main_layout.addWidget(select_label)
        main_layout.addSpacing(20)

        if "Germany" in self.event_name:
            self.add_germany_specific_widgets(main_layout)
        else:
            self.add_general_seating_buttons(main_layout)

        self.setLayout(main_layout)

        # Set window background color
        self.set_background_gradient()

    def create_split_title_label(self):
        font = QFont('Playfair Display', 28)
        first_line, second_line = self.split_title(self.event_name)

        event_label = QLabel(f"{first_line}\n{second_line}")
        event_label.setFont(font)
        event_label.setStyleSheet("color: #2c3e50; border-bottom: 2px solid #34495e; padding-bottom: 10px;")
        event_label.setAlignment(Qt.AlignCenter)
        return event_label

    def split_title(self, title):
        if "-" in title:
            parts = title.split("-", 1)
            return parts[0].strip(), parts[1].strip()  # Removed the "-" from the second part
        else:
            words = title.split()
            mid = len(words) // 2
            return " ".join(words[:mid]), " ".join(words[mid:])

    def add_germany_specific_widgets(self, layout):
        # Stadium image
        image_label = QLabel(self)
        pixmap = QPixmap('stadium_seats.png').scaled(330, 330, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        # Seat input
        seat_input = QLineEdit(self)
        seat_input.setPlaceholderText("Enter your seat number")
        seat_input.setFont(QFont('Helvetica', 14))
        seat_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                background-color: white;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                margin-top: 20px;
            }
        """)
        layout.addWidget(seat_input)

        # Confirm button
        confirm_button = QPushButton("Confirm Seat")
        confirm_button.setFont(QFont('Helvetica', 16))
        confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        confirm_button.clicked.connect(lambda: self.select_seating_area(seat_input.text()))
        layout.addWidget(confirm_button)

    def add_general_seating_buttons(self, layout):
        seating_areas = ["VIP", "Premium", "Standard", "Economy"]
        
        for area in seating_areas:
            area_button = QPushButton(area)
            area_button.setFont(QFont('Helvetica', 16))
            area_button.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            area_button.clicked.connect(lambda checked, a=area: self.select_seating_area(a))
            layout.addWidget(area_button)

    def set_background_gradient(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor('#ecf0f1'))
        gradient.setColorAt(1.0, QColor('#bdc3c7'))
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

    def select_seating_area(self, area):
        self.seating_area = area
        print(f"Selected seating area: {area}")
        self.home_page = HomePage(self.event_name, self.seating_area, ongoing_request_count=0)
        self.home_page.show()
        self.close()


################### HOME PAGE ###################
class HomePage(QWidget):
    def __init__(self, event_name, seating_area, ongoing_request_count=0, order_placed=False):
        super().__init__()
        self.setWindowTitle("EventEats - Home")
        self.setFixedSize(400, 700)
        self.order_placed = order_placed
        self.event_name = event_name
        self.seating_area = seating_area
        self.current_order = None
        self.request_count = 0
        self.ongoing_request_count = ongoing_request_count
        self.button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#active {
                background-color: #2980b9;
            }
        """
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Welcome label
        welcome_label = QLabel("Welcome to EventEats!", self)
        welcome_label.setFont(QFont('Roboto', 24, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("color: #2c3e50; margin-bottom: 30px;")

        # Event and Seat Information
        event_info = QLabel(f"Event: {self.event_name}", self)
        event_info.setFont(QFont('Roboto', 16))
        event_info.setAlignment(Qt.AlignCenter)
        event_info.setStyleSheet("color: #34495e; margin-bottom: 10px;")

        seat_info = QLabel(f"Seat: {self.seating_area}", self)
        seat_info.setFont(QFont('Roboto', 16))
        seat_info.setAlignment(Qt.AlignCenter)
        seat_info.setStyleSheet("color: #34495e; margin-bottom: 30px;")

        # Place an order button
        order_button = QPushButton("Place an order", self)
        order_button.setFont(QFont('Roboto', 18))
        order_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        order_button.clicked.connect(self.place_order)

        # Open Requests button
        self.requests_button = BadgeButton("Open Requests")
        self.requests_button.setFont(QFont('Roboto', 18))
        self.requests_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.requests_button.clicked.connect(self.show_requests)
        self.requests_button.setBadgeCount(self.request_count)

        # Ongoing requests button (initially not visible)
        self.ongoing_requests_button = QPushButton(f"Ongoing Requests (0)", self)
        self.ongoing_requests_button.setFont(QFont('Roboto', 18))
        self.ongoing_requests_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.ongoing_requests_button.clicked.connect(self.show_ongoing_requests)
        self.ongoing_requests_button.hide()  # Initially hidden

        self.orders_placed_button = QPushButton("Orders Placed", self)
        self.orders_placed_button.setFont(QFont('Roboto', 18))
        self.orders_placed_button.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)
        self.orders_placed_button.clicked.connect(self.show_orders_placed)
        self.orders_placed_button.hide()

        # Logo and company name
        logo_label = QLabel(self)
        pixmap = QPixmap("company_logo.png").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        company_name_label = QLabel("EventEats", self)
        company_name_label.setAlignment(Qt.AlignCenter)
        company_name_label.setFont(QFont('Roboto', 36, QFont.Bold))
        company_name_label.setStyleSheet("color: #2c3e50; margin-top: 20px;")

        # Footer with buttons
        footer = QWidget()
        footer_layout = QHBoxLayout(footer)

        buttons = ["Home", "Settings", "Invite"]
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(self.button_style)
            if button_text == "Home":
                button.setObjectName("active")
            footer_layout.addWidget(button)

        # Adding widgets to layout
        main_layout.addWidget(welcome_label)
        main_layout.addWidget(event_info)
        main_layout.addWidget(seat_info)
        main_layout.addWidget(order_button)
        main_layout.addWidget(self.requests_button)
        main_layout.addWidget(self.ongoing_requests_button)
        main_layout.addWidget(self.orders_placed_button)
        main_layout.addStretch(1)
        main_layout.addWidget(logo_label)
        main_layout.addWidget(company_name_label)
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

        #self.update_request_count(0)
        self.update_ongoing_request_count(self.ongoing_request_count)

        if self.order_placed:
            self.orders_placed_button.show()

    def update_request_count(self, count):
        self.request_count = count
        self.requests_button.setBadgeCount(count)

    def set_current_order(self, order):
        self.current_order = order
        self.update_ongoing_request_count(1)

    def update_ongoing_request_count(self, count):
        self.ongoing_request_count = count
        if count > 0:
            self.ongoing_requests_button.setText(f"Ongoing Requests ({count})")
            self.ongoing_requests_button.show()
        else:
            self.ongoing_requests_button.hide()

    def show_requests(self):
        self.requests_page = RequestsPage(self.event_name, self.seating_area)
        self.requests_page.show()
        self.close()

    def place_order(self):
        self.order_page = OrderHomePage(self.event_name, self.seating_area)
        self.order_page.show()
        self.close()

    def show_ongoing_requests(self):
        if self.current_order:
            self.ongoing_requests_page = OngoingRequestsPage(self.current_order, self.event_name, self.seating_area)
            self.ongoing_requests_page.show()
            self.close()
        else:
            QMessageBox.information(self, "No Ongoing Requests", "You don't have any ongoing requests at the moment.")

    def show_orders_placed(self):
        self.orders_placed_page = OrdersPlacedPage(self.event_name, self.seating_area)
        self.orders_placed_page.show()
        self.close()

################### ORDER PAGE ###################
class OrderHomePage(QWidget):
    def __init__(self, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Order")
        self.setFixedSize(400, 700)
        self.event_name = event_name
        self.seating_area = seating_area
        self.cart = {}
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        # Event and seating area info
        info_card = QWidget()
        info_card.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        """)
        info_layout = QVBoxLayout(info_card)
        
        main_layout.addWidget(back_button)
        
        event_label = QLabel(self.event_name)
        event_label.setFont(QFont('Roboto', 18, QFont.Bold))
        event_label.setStyleSheet("color: #3498db;")
        
        seat_label = QLabel(f"Seat: {self.seating_area}")
        seat_label.setFont(QFont('Roboto', 14))
        seat_label.setStyleSheet("color: #2ecc71;")
        
        info_layout.addWidget(event_label)
        info_layout.addWidget(seat_label)
        
        main_layout.addWidget(info_card)

        # Menu items
        menu_items = [
            {"name": "Hot Dog", "price": 5, "icon": "🌭"},
            {"name": "Burger", "price": 8, "icon": "🍔"},
            {"name": "Pizza Slice", "price": 4, "icon": "🍕"},
            {"name": "Soda", "price": 3, "icon": "🥤"},
            {"name": "Popcorn", "price": 4, "icon": "🍿"},
            {"name": "Beer", "price": 6, "icon": "🍺"},
            {"name": "Nachos", "price": 5, "icon": "🧀"},
            {"name": "Pretzel", "price": 3, "icon": "🥨"},
            {"name": "Ice Cream", "price": 4, "icon": "🍦"},
            {"name": "Cotton Candy", "price": 3, "icon": "🍭"},
            {"name": "Chicken Tenders", "price": 7, "icon": "🍗"},
            {"name": "French Fries", "price": 4, "icon": "🍟"},
        ]

        menu_scroll = QScrollArea()
        menu_scroll.setWidgetResizable(True)
        menu_scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: rgba(241, 241, 241, 0.5);
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: rgba(136, 136, 136, 0.5);
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)

        menu_widget = QWidget()
        menu_layout = QVBoxLayout(menu_widget)

        for item in menu_items:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)

            item_name = QLabel(f"{item['icon']} {item['name']}")
            item_name.setFont(QFont('Roboto', 14))
            item_price = QLabel(f"${item['price']}")
            item_price.setFont(QFont('Roboto', 14))
            item_price.setStyleSheet("color: #e74c3c;")
            
            add_button = QPushButton("+")
            add_button.setFixedSize(30, 30)
            add_button.setStyleSheet("""
                QPushButton {
                    background-color: #2ecc71;
                    color: white;
                    border-radius: 15px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #27ae60;
                }
            """)
            add_button.clicked.connect(lambda checked, i=item: self.add_to_cart(i))

            remove_button = QPushButton("-")
            remove_button.setFixedSize(30, 30)
            remove_button.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border-radius: 15px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
            """)
            remove_button.clicked.connect(lambda checked, i=item: self.remove_from_cart(i))

            item_layout.addWidget(item_name)
            item_layout.addStretch(1)
            item_layout.addWidget(item_price)
            item_layout.addWidget(add_button)
            item_layout.addWidget(remove_button)

            menu_layout.addWidget(item_widget)

        menu_scroll.setWidget(menu_widget)
        main_layout.addWidget(menu_scroll)

        # Cart summary
        self.cart_summary = QLabel("Total: $0.00")
        self.cart_summary.setFont(QFont('Roboto', 16, QFont.Bold))
        self.cart_summary.setAlignment(Qt.AlignCenter)
        self.cart_summary.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        """)
        main_layout.addWidget(self.cart_summary)

        # Checkout button
        review_button = QPushButton("Review Order")
        review_button.setFont(QFont('Roboto', 16))
        review_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        review_button.clicked.connect(self.review_order)
        main_layout.addWidget(review_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def add_to_cart(self, item):
        if item["name"] in self.cart:
            self.cart[item["name"]]["quantity"] += 1
        else:
            self.cart[item["name"]] = {"price": item["price"], "quantity": 1}
        self.update_cart_summary()

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.show()
        self.close()

    def remove_from_cart(self, item):
        if item["name"] in self.cart:
            if self.cart[item["name"]]["quantity"] > 1:
                self.cart[item["name"]]["quantity"] -= 1
            else:
                del self.cart[item["name"]]
        self.update_cart_summary()

    def update_cart_summary(self):
        total = sum(item["price"] * item["quantity"] for item in self.cart.values())
        self.cart_summary.setText(f"Total: ${total:.2f}")

    def review_order(self):
        if not self.cart:
            QMessageBox.information(self, "Review Order", "Your cart is empty. Please add items to your cart.")
        else:
            self.review_page = ReviewOrderPage(self.cart, self.event_name, self.seating_area)
            self.review_page.show()
            self.close()


################### REVIEW ORDER PAGE ###################
class ReviewOrderPage(QWidget):
    def __init__(self, cart, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Review Order")
        self.setFixedSize(400, 700)
        self.cart = cart
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)

        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)


        # Event and seating area info
        info_card = QWidget()
        info_card.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        """)
        info_layout = QVBoxLayout(info_card)
        
        event_label = QLabel(self.event_name)
        event_label.setFont(QFont('Roboto', 18, QFont.Bold))
        event_label.setStyleSheet("color: #3498db;")
        
        seat_label = QLabel(f"Seat: {self.seating_area}")
        seat_label.setFont(QFont('Roboto', 14))
        seat_label.setStyleSheet("color: #2ecc71;")

        info_layout.addWidget(event_label)
        info_layout.addWidget(seat_label)
        
        main_layout.addWidget(info_card)

        # Order summary
        order_summary = QScrollArea()
        order_summary.setWidgetResizable(True)
        order_summary.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
            }
        """)

        summary_widget = QWidget()
        summary_layout = QVBoxLayout(summary_widget)

        for item_name, details in self.cart.items():
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)

            item_label = QLabel(f"{item_name} x{details['quantity']}")
            item_label.setFont(QFont('Roboto', 14))
            
            price_label = QLabel(f"${details['price'] * details['quantity']:.2f}")
            price_label.setFont(QFont('Roboto', 14))
            price_label.setAlignment(Qt.AlignRight)

            item_layout.addWidget(item_label)
            item_layout.addWidget(price_label)

            summary_layout.addWidget(item_widget)

        order_summary.setWidget(summary_widget)
        main_layout.addWidget(order_summary)

        # Total
        total = sum(item["price"] * item["quantity"] for item in self.cart.values())
        total_label = QLabel(f"Total: ${total:.2f}")
        total_label.setFont(QFont('Roboto', 18, QFont.Bold))
        total_label.setAlignment(Qt.AlignCenter)
        total_label.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        """)
        main_layout.addWidget(total_label)

        button_layout = QHBoxLayout()

        edit_order_button = QPushButton("Edit Order")
        edit_order_button.setFont(QFont('Roboto', 16))
        edit_order_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        edit_order_button.clicked.connect(self.edit_order)

        place_order_button = QPushButton("Place Order")
        place_order_button.setFont(QFont('Roboto', 16))
        place_order_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)

        place_order_button.clicked.connect(self.place_order)

        button_layout.addWidget(edit_order_button)
        button_layout.addWidget(place_order_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def edit_order(self):
        self.order_page = OrderHomePage(self.event_name, self.seating_area)
        self.order_page.cart = self.cart
        self.order_page.update_cart_summary()
        self.order_page.show()
        self.close()

    def place_order(self):
        QMessageBox.information(self, "Order Placed", "Your order has been placed successfully!")
        self.home_page = HomePage(self.event_name, self.seating_area, order_placed=True)
        self.home_page.show()
        self.close()

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.show()
        self.close()

class BadgeButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.badge_count = 0

    def setBadgeCount(self, count):
        self.badge_count = count
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.badge_count > 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            badge_size = 24
            badge_x = self.width() - badge_size - 5
            badge_y = 5
            
            # Draw red circle
            painter.setBrush(QBrush(QColor("red")))
            painter.setPen(QPen(Qt.NoPen))
            painter.drawEllipse(badge_x, badge_y, badge_size, badge_size)
            
            # Draw number
            painter.setPen(QPen(QColor("white")))
            painter.setFont(QFont('Arial', 10, QFont.Bold))
            painter.drawText(QRect(badge_x, badge_y, badge_size, badge_size), 
                             Qt.AlignCenter, str(self.badge_count))
            

################### REQUESTS PAGE ###################
class RequestsPage(QWidget):
    def __init__(self, event_name, seating_area, parent=None):
        super().__init__(parent)
        self.setWindowTitle("EventEats - Open Requests")
        self.setFixedSize(400, 700)
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)
        # Title
        title_label = QLabel("Open Requests", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Scrollable area for requests
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: rgba(241, 241, 241, 0.5);
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: rgba(136, 136, 136, 0.5);
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Generate 5 example requests
        for _ in range(5):
            request_widget = self.create_request_widget()
            scroll_layout.addWidget(request_widget)

        scroll_area.setWidget(scroll_content)

        # Back button
        back_button = QPushButton("Back to Home", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        main_layout.addWidget(title_label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def create_request_widget(self):
        request_widget = QFrame()
        request_widget.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                padding: 10px;
                margin: 5px 0;
            }
        """)
        request_layout = QVBoxLayout(request_widget)

        # Generate random data for the request
        seat_number = f"Seat {random.randint(1, 100)}"
        items = [
            ("🌭 Hot Dog", random.randint(3, 6)),
            ("🍔 Burger", random.randint(5, 9)),
            ("🍟 Fries", random.randint(2, 4)),
            ("🥤 Soda", random.randint(2, 3)),
            ("🍕 Pizza Slice", random.randint(3, 5)),
            ("🍿 Popcorn", random.randint(3, 5)),
            ("🍺 Beer", random.randint(5, 8))
        ]
        order = random.sample(items, k=random.randint(1, len(items)))
        price = sum([item[1] for item in order])
        profit = round(price * 0.2, 2)
        distance_to_seat = random.randint(0, 350)
        distance_to_store = random.randint(0, 350)

        # Create labels for the request information
        seat_label = QLabel(seat_number)
        seat_label.setFont(QFont('Roboto', 16, QFont.Bold))
        
        order_label = QLabel(", ".join([f"{item[0]} (${item[1]})" for item in order]))
        order_label.setFont(QFont('Roboto', 10))
        order_label.setWordWrap(True)
        
        price_label = QLabel(f"💰 Total: ${price}")
        price_label.setFont(QFont('Roboto', 14))
        
        profit_label = QLabel(f"💼 Profit: ${profit}")
        profit_label.setFont(QFont('Roboto', 14))
        
        distance_to_seat_label = QLabel(f"🚶 Distance to customer: {distance_to_seat}m")
        distance_to_seat_label.setFont(QFont('Roboto', 14))

        distance_to_store_label = QLabel(f"🏪 Distance to store: {distance_to_store}m")
        distance_to_store_label.setFont(QFont('Roboto', 14))

        request_layout.addWidget(seat_label)
        request_layout.addWidget(order_label)
        request_layout.addWidget(price_label)
        request_layout.addWidget(profit_label)
        request_layout.addWidget(distance_to_seat_label)
        request_layout.addWidget(distance_to_store_label)

        # Create an order dictionary
        order_dict = {
            'seat': seat_number,
            'items': order,
            'price': price,
            'profit': profit,
            'distance_to_seat': distance_to_seat,
            'distance_to_store': distance_to_store
        }

        # Make the widget clickable
        request_widget.mousePressEvent = lambda event: self.open_order_detail(order_dict)

        return request_widget

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.show()
        self.close()

    def open_order_detail(self, order):
        self.order_detail_page = OrderDetailPage(order, self.event_name, self.seating_area)
        self.order_detail_page.show()
        self.close()


################### ORDER DETAIL PAGE ###################
class OrderDetailPage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Order Detail")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Order Detail", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Order details
        details_widget = QWidget()
        details_widget.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 15px;
        """)
        details_layout = QVBoxLayout(details_widget)

        seat_label = QLabel(f"{self.order['seat']}")
        seat_label.setFont(QFont('Roboto', 16, QFont.Bold))
        
        for item in self.order['items']:
            item_label = QLabel(f"{item[0]} (${item[1]})")
            item_label.setFont(QFont('Roboto', 12))
            details_layout.addWidget(item_label)

        total_label = QLabel(f"Total: ${self.order['price']}")
        total_label.setFont(QFont('Roboto', 14, QFont.Bold))
        
        profit_label = QLabel(f"Profit: ${self.order['profit']}")
        profit_label.setFont(QFont('Roboto', 14, QFont.Bold))
        
        distance_to_seat_label = QLabel(f"Distance to customer: {self.order['distance_to_seat']}m")
        distance_to_seat_label.setFont(QFont('Roboto', 14))

        distance_to_store_label = QLabel(f"Distance to store: {self.order['distance_to_store']}m")
        distance_to_store_label.setFont(QFont('Roboto', 14))

        details_layout.addWidget(seat_label)
        details_layout.addWidget(total_label)
        details_layout.addWidget(profit_label)
        details_layout.addWidget(distance_to_seat_label)
        details_layout.addWidget(distance_to_store_label)

        # Buttons
        button_layout = QHBoxLayout()

        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        back_button.clicked.connect(self.go_back)

        accept_button = QPushButton("Accept Order", self)
        accept_button.setFont(QFont('Roboto', 16))
        accept_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        accept_button.clicked.connect(self.accept_order)

        button_layout.addWidget(back_button)
        button_layout.addWidget(accept_button)

        main_layout.addWidget(title_label)
        main_layout.addWidget(details_widget)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def go_back(self):
        self.requests_page = RequestsPage(self.event_name, self.seating_area)
        self.requests_page.show()
        self.close()

    def accept_order(self):
        self.accept_order_page = AcceptOrderPage(self.order, self.event_name, self.seating_area)
        self.accept_order_page.show()
        self.close()

################### ACCEPT ORDER PAGE ###################
class AcceptOrderPage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Accept Order")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        # Title
        title_label = QLabel("Estimate Arrival Time", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Time picker
        self.time_picker = QTimeEdit(self)
        self.time_picker.setDisplayFormat("hh:mm")
        self.time_picker.setFont(QFont('Roboto', 36))
        self.time_picker.setStyleSheet("""
            QTimeEdit {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                padding: 20px;
            }
        """)

        # Confirm button
        confirm_button = QPushButton("Confirm", self)
        confirm_button.setFont(QFont('Roboto', 18))
        confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        confirm_button.clicked.connect(self.confirm_order)

        main_layout.addWidget(title_label)
        main_layout.addWidget(self.time_picker)
        main_layout.addWidget(confirm_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def confirm_order(self):
        estimated_time = self.time_picker.time().toString("hh:mm")
        QMessageBox.information(self, "Order Accepted", f"You have accepted the order. Estimated arrival time is in {estimated_time} minutes.")
        
        # Create a new HomePage instance and set the current order
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.set_current_order(self.order)
        self.home_page.show()
        self.close()

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.show()
        self.close()

class OngoingRequestsPage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Ongoing Request")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        # Title
        title_label = QLabel("Ongoing Request", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Order details
        details_widget = QWidget()
        details_widget.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 15px;
        """)
        details_layout = QVBoxLayout(details_widget)

        seat_label = QLabel(f"Seat: {self.order['seat']}")
        seat_label.setFont(QFont('Roboto', 16, QFont.Bold))
        
        items_label = QLabel("Items:")
        items_label.setFont(QFont('Roboto', 14, QFont.Bold))
        
        for item in self.order['items']:
            item_label = QLabel(f"  • {item[0]} (${item[1]})")
            item_label.setFont(QFont('Roboto', 12))
            details_layout.addWidget(item_label)

        total_label = QLabel(f"Total: ${self.order['price']}")
        total_label.setFont(QFont('Roboto', 14, QFont.Bold))

        details_layout.addWidget(seat_label)
        details_layout.addWidget(items_label)
        details_layout.addWidget(total_label)

        # Buttons
        chat_button = QPushButton("Chat with Receiver", self)
        chat_button.setFont(QFont('Roboto', 16))
        chat_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        chat_button.clicked.connect(self.open_chat)

        navigate_button = QPushButton("Navigate to Delivery", self)
        navigate_button.setFont(QFont('Roboto', 16))
        navigate_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        navigate_button.clicked.connect(self.open_navigation)

        enter_code_button = QPushButton("Enter Code", self)
        enter_code_button.setFont(QFont('Roboto', 16))
        enter_code_button.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)
        enter_code_button.clicked.connect(self.open_enter_code)

        main_layout.addWidget(title_label)
        main_layout.addWidget(details_widget)
        main_layout.addWidget(chat_button)
        main_layout.addWidget(navigate_button)
        main_layout.addWidget(enter_code_button)
        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def open_chat(self):
        self.chat_page = ChatPage(self.order, self.event_name, self.seating_area)
        self.chat_page.show()
        self.close()

    def open_navigation(self):
        self.navigation_page = NavigationPage(self.order, self.event_name, self.seating_area)
        self.navigation_page.show()
        self.close()

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area)
        self.home_page.show()
        self.close()

    def open_enter_code(self):
        self.enter_code_page = EnterCodePage(self.order, self.event_name, self.seating_area)
        self.enter_code_page.show()
        self.close()

class ChatPage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Chat")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Chat with Receiver", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Placeholder for chat functionality
        chat_placeholder = QLabel("Chat functionality will be implemented here.")
        chat_placeholder.setFont(QFont('Roboto', 16))
        chat_placeholder.setAlignment(Qt.AlignCenter)
        chat_placeholder.setWordWrap(True)

        # Back button
        back_button = QPushButton("Back to Ongoing Request", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        main_layout.addWidget(title_label)
        main_layout.addWidget(chat_placeholder)
        main_layout.addStretch(1)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def go_back(self):
        self.ongoing_requests_page = OngoingRequestsPage(self.order, self.event_name, self.seating_area)
        self.ongoing_requests_page.show()
        self.close()

class NavigationPage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Navigation")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Navigation", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Placeholder for navigation functionality
        navigation_placeholder = QLabel("Navigation functionality will be implemented here.")
        navigation_placeholder.setFont(QFont('Roboto', 16))
        navigation_placeholder.setAlignment(Qt.AlignCenter)
        navigation_placeholder.setWordWrap(True)

        # Back button
        back_button = QPushButton("Back to Ongoing Request", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        main_layout.addWidget(title_label)
        main_layout.addWidget(navigation_placeholder)
        main_layout.addStretch(1)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def go_back(self):
        self.ongoing_requests_page = OngoingRequestsPage(self.order, self.event_name, self.seating_area)
        self.ongoing_requests_page.show()
        self.close()

class OrdersPlacedPage(QWidget):
    def __init__(self, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Orders Placed")
        self.setFixedSize(400, 700)
        self.event_name = event_name
        self.seating_area = seating_area
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Orders Placed", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Scrollable area for orders
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: rgba(241, 241, 241, 0.5);
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: rgba(136, 136, 136, 0.5);
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Example order (you should replace this with actual order data)
        order_widget = self.create_order_widget({
            'items': [('🌭 Hot Dog', 5), ('🍟 Fries', 3), ('🥤 Soda', 2)],
            'price': 10,
            'status': 'Pending'
        })
        scroll_layout.addWidget(order_widget)

        scroll_area.setWidget(scroll_content)

        # Back button
        back_button = QPushButton("Back to Home", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        back_button.clicked.connect(self.go_back)

        main_layout.addWidget(title_label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def create_order_widget(self, order):
        order_widget = QFrame()
        order_widget.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                padding: 10px;
                margin: 5px 0;
            }
        """)
        order_layout = QVBoxLayout(order_widget)

        items_label = QLabel(", ".join([f"{item[0]} (${item[1]})" for item in order['items']]))
        items_label.setFont(QFont('Roboto', 12))
        items_label.setWordWrap(True)

        price_label = QLabel(f"Total: ${order['price']}")
        price_label.setFont(QFont('Roboto', 14, QFont.Bold))

        status_label = QLabel(f"Status: {order['status']}")
        status_label.setFont(QFont('Roboto', 14))
        status_label.setStyleSheet(f"color: {'#e74c3c' if order['status'] == 'Pending' else '#2ecc71'};")

        # Generate and display a random 4-digit code
        code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        code_label = QLabel(f"Verification Code: {code}")
        code_label.setFont(QFont('Roboto', 14, QFont.Bold))
        code_label.setStyleSheet("color: #3498db;")

        order_layout.addWidget(items_label)
        order_layout.addWidget(price_label)
        order_layout.addWidget(status_label)
        order_layout.addWidget(code_label)

        return order_widget

    def go_back(self):
        self.home_page = HomePage(self.event_name, self.seating_area, order_placed=True)
        self.home_page.show()
        self.close()


class EnterCodePage(QWidget):
    def __init__(self, order, event_name, seating_area):
        super().__init__()
        self.setWindowTitle("EventEats - Enter Code")
        self.setFixedSize(400, 700)
        self.order = order
        self.event_name = event_name
        self.seating_area = seating_area
        self.code = ['', '', '', '']
        self.current_digit = 0
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Enter Verification Code", self)
        title_label.setFont(QFont('Roboto', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")

        # Code entry display
        self.code_display = QLabel("• • • •")
        self.code_display.setFont(QFont('Roboto', 36, QFont.Bold))
        self.code_display.setAlignment(Qt.AlignCenter)
        self.code_display.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 20px;
        """)

        # Number pad
        numpad_layout = QGridLayout()
        numbers = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '', '0', 'Del'
        ]

        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, number in zip(positions, numbers):
            if number:
                button = QPushButton(number)
                button.setFont(QFont('Roboto', 18))
                button.setFixedSize(80, 80)
                button.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(52, 152, 219, 0.8);
                        color: white;
                        border-radius: 40px;
                    }
                    QPushButton:hover {
                        background-color: rgba(41, 128, 185, 0.9);
                    }
                """)
                if number == 'Del':
                    button.clicked.connect(self.delete_digit)
                else:
                    button.clicked.connect(lambda _, num=number: self.enter_digit(num))
                numpad_layout.addWidget(button, *position)

        # Back button
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont('Roboto', 16))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        back_button.clicked.connect(self.go_back)

        main_layout.addWidget(title_label)
        main_layout.addWidget(self.code_display)
        main_layout.addLayout(numpad_layout)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

        # Set background image
        background = QLabel(self)
        background.setPixmap(QPixmap("food.png").scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        background.setGeometry(self.rect())
        background.lower()

    def enter_digit(self, digit):
        if self.current_digit < 4:
            self.code[self.current_digit] = digit
            self.current_digit += 1
            self.update_code_display()
            if self.current_digit == 4:
                self.verify_code()

    def delete_digit(self):
        if self.current_digit > 0:
            self.current_digit -= 1
            self.code[self.current_digit] = ''
            self.update_code_display()

    def update_code_display(self):
        display = ''
        for digit in self.code:
            display += '• ' if digit == '' else f'{digit} '
        self.code_display.setText(display.strip())

    def verify_code(self):
        entered_code = ''.join(self.code)
        # In a real application, you would verify this code against the actual code for the order
        if entered_code == '1234':  # Replace with actual verification logic
            QMessageBox.information(self, "Success", "Code verified successfully!")
            self.go_back()
        else:
            QMessageBox.warning(self, "Error", "Incorrect code. Please try again.")
            self.code = ['', '', '', '']
            self.current_digit = 0
            self.update_code_display()

    def go_back(self):
        self.ongoing_requests_page = OngoingRequestsPage(self.order, self.event_name, self.seating_area)
        self.ongoing_requests_page.show()
        self.close()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())