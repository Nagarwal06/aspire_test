#Commom Constants to be used in Products
web_url = "https://aspireapp.odoo.com"
user = "user@aspireapp.com"
password = '@sp1r3app'
refresh_tout = 20
product_name = "Test_Product"
browser_name = "chrome"
username_css = "input[id=login]"
password_css = "input[id=password]"
login_btn_css = "button[type=submit]"
timeout = 30

# Product XPATHs and CSSs
inventory_xpath = ".//div[.='Inventory']"
top_meu_bar_css = "nav[class=o_main_navbar]"
products_menu_xpath = ".//button[contains(@data-menu-xmlid, 'stock.menu_stock_inventory_control')]"
products_item_xpath = ".//a[contains(@data-menu-xmlid, 'stock.menu_product_variant_config_stock')]"
create_btn_xpath = ".//button[contains(text(), 'Create')]"
product_name_xpath = ".//input[contains(@name, 'name')]"
save_btn_xpath = ".//button[contains(text(), 'Save')]"
update_btn_xpath = ".//button[@name='action_update_quantity_on_hand']"
selected_row  = ".//tbody/tr[contains(@class,'o_data_row')]"
row_location = "%s//div[@name='location_id']" % selected_row
available_location = ".//ul[contains(@class, 'ui-menu')]//li/a"
item_quality = "%s//td[6]//input" % selected_row

# Manufacturing XPATHs
application_icon_css = "a[title='Home menu']"
manufacturing_xpath = ".//div[.='Manufacturing']"
product_name_dropdown_xpath = ".//div[@name='product_id']//input"
suggestion_item = ".//ul[contains(@class, 'ui-menu') and contains(@style, 'top')]//li/a[contains(text(), '%s')]"
active_table_xpath = ".//div[@class='tab-pane active']//table"
add_component_btn_xpath = "%s//a[text()='Add a line']" % active_table_xpath
row_component = "%s//tbody/tr[contains(@class, 'o_selected_row')]" % active_table_xpath
suggestion_dropdown = ".//ul[contains(@class, 'ui-menu') and contains(@style, 'top')]"
product_xpath = "./td[1]//input"
quantity_xpath = './/td[3]//input'
confirm_btn_xpath = ".//button/span[contains(text(), 'Confirm')]"
mark_as_done_btn_xpath = ".//button/span[contains(text(), 'Mark as Done')]"
apply_btn_xpath = ".//button/span[contains(text(), 'Apply')]"
modal_dialog_xpath = ".//div[contains(@class, 'modal-dialog')]"
status_bar_xpath = ".//div[contains(@class, 'o_statusbar_status')]"
current_status_xpath = "%s/button[@title='Current state']" % status_bar_xpath
row_component_xpath = "%s/tbody/tr[@class='o_data_row']" % active_table_xpath

#verify order XPATHs
verify_product_name_xpath = ".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//td[@name='product_id']"
verify_product_to_consume_xpath = ".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//span[@name='product_uom_qty']"
verify_product_consumed_xpath = ".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//td[@name='quantity_done']"