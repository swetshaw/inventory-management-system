# inventory-management-system

This project implements an inventory management system using Flask

## Installation
### Clone the repository
```
git clone https://github.com/swetshaw/inventory-management-system.git
```
### Enter into the folder
```
cd inventory-management-system
```
### Install required libraries
```
pip3 install -r requirements.txt
```
### Initialize the database
```
flask init-db
```
### Run the application
```
flask run
```
## Demo
#### Dashboard
Following page opens up when `flask run` is executed. This is called the **Dashboard** page. It displays the product quantity in each location.

![image](https://user-images.githubusercontent.com/26214362/120144652-f370a880-c1ff-11eb-906e-3ed4eb3bbbd1.png)

#### Products
This page shows all the products listed for the inventory. 
- Features
  - Add product
  - Edit product

![image](https://user-images.githubusercontent.com/26214362/120145086-9de8cb80-c200-11eb-9a03-a0f720b1921e.png)

#### Location
This page is similar to the products page where all the location of the inventory is listed.
- Features
  - Add Location
  - Edit Location
 
![image](https://user-images.githubusercontent.com/26214362/120145428-20718b00-c201-11eb-9ae4-bb4f30b13405.png)

#### Product Movement
On this page, the user can move the product from one location to another. 
- Features
  - Move Product
 
![image](https://user-images.githubusercontent.com/26214362/120145912-e81e7c80-c201-11eb-907b-8eb9f0ae986b.png)
