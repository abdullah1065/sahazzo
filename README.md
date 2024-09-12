# Sahazzo

## Website Link: 
https://sahazzo.vercel.app


<a href="https://ibb.co/L8SLD6T"><img src="https://i.ibb.co/t4B7wc0/Home-page-01.png" alt="Home-page-01" border="0"></a>


## Overview

SAHAZZO is a donation management system designed to streamline the process of collecting, managing, and distributing donations through various events. The system allows administrators, organizers, volunteers, and donors to collaborate efficiently for charitable causes.

## Key Modules

1. **Donator**
    - **Attributes**:
        - First Name
        - Last Name
        - NID
        - Phone Number
        - Email
        - Password
    - **Functionality**:
        - Donators can make donations by entering payment details and checking the current fund status.

2. **Organizer**
    - **Attributes**:
        - First Name
        - Last Name
        - NID
        - Phone Number
        - Email
        - Password
    - **Functionality**:
        - Organizers can manage events and keep track of donations.

3. **Volunteer**
    - **Attributes**:
        - First Name
        - Last Name
        - NID
        - Phone Number
        - Email
        - Password
        - Location
        - Status
    - **Functionality**:
        - Volunteers manage event logistics, including item collection and delivery.

4. **Event**
    - **Attributes**:
        - Event ID
        - Name
        - Location
        - Budget
        - Preferred Shop
        - Start Time
        - End Time
        - Item Request
        - Created By
    - **Functionality**:
        - Organizers can create and manage events.

5. **Items**
    - **Attributes**:
        - Event ID
        - Name
        - Quantity
    - **Functionality**:
        - Items required for events can be listed and tracked.

6. **Fund**
    - **Attributes**:
        - Event ID
        - Amount
        - Status
        - Fund For
        - Fund Taken By
    - **Functionality**:
        - Fundraising is tracked per event, including the amount raised and its purpose.

7. **Admin**
    - **Attributes**:
        - Name
        - Admin ID
        - Email
        - Password
    - **Functionality**:
        - Administrators can oversee all activities, manage users, and ensure the smooth operation of the platform.

8. **Shop**
    - **Attributes**:
        - Shop ID
        - Event ID
        - Pay Demand
        - Delivery Status
    - **Functionality**:
        - Shops provide items required for the events and keep track of payments and delivery.

## System Features

- **User Authentication**: Secure registration and login for Donators, Organizers, Volunteers, and Admins.
- **Donation Tracking**: Donators can view their contributions, and Organizers can track the funds raised.
- **Event Management**: Organizers can create and manage events, including budget, item requests, and volunteers.
- **Item Management**: Track the items required and donated for each event.
- **Fund Management**: Manage the allocation of raised funds for specific events and purposes.
- **Shop Management**: Collaborate with shops to purchase and deliver necessary items for the event.

## Usage

1. **Donator**: Make donations to specific events and track your donation status.
2. **Organizer**: Create and manage events, request items, and track donations.
3. **Volunteer**: Assist in event logistics and delivery of items.
4. **Admin**: Oversee the entire system and ensure the efficient management of events and donations.

## Technologies Used

<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p>


## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/sahazzo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd sahazzo
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

8. Access the site at `http://127.0.0.1:8000/`.
