
refresh_tout = 20
product_name = "Test_Product"
BROWSER_NAME = "chrome"
username_css = "input[id=login]"
password_css = "input[id=password]"
loginbutton_css = "button[type=submit]"
timeout = 30
user = "user@aspireapp.com"
password = '@sp1r3app'

# Product XPATHs
inventory_xpath = ".//div[.='Inventory']"
top_meu_bar_css = "nav[class=o_main_navbar]"
products_menu_xpath = ".//button[contains(@data-menu-xmlid, 'stock.menu_stock_inventory_control')]"
products_item_xpath = ".//a[contains(@data-menu-xmlid, 'stock.menu_product_variant_config_stock')]"
create_button_xpath = ".//button[contains(text(), 'Create')]"
product_name_xpath = ".//input[contains(@name, 'name')]"
save_button_xpath = ".//button[contains(text(), 'Save')]"
update_button_xpath = ".//button[@name='action_update_quantity_on_hand']"
SELECTED_ROW = ".//tbody/tr[contains(@class,'o_data_row')]"
LOCATION_ROW = "%s//div[@name='location_id']" % SELECTED_ROW
AVAILABLE_LOCATION = ".//ul[contains(@class, 'ui-menu')]//li/a"
ITEM_QUALITY = "%s//td[6]//input" % SELECTED_ROW

# Manufacturing XPATHs
application_icon_css = "a[title='Home menu']"
manufacturing_xpath = ".//div[.='Manufacturing']"
PRODUCT_NAME_DROPDOWN_XPATH = ".//div[@name='product_id']//input"
SUGGESTION_ITEM = ".//ul[contains(@class, 'ui-menu') and contains(@style, 'top')]//li/a[contains(text(), '%s')]"
ACTIVE_TABLE_XPATH = ".//div[@class='tab-pane active']//table"
ADD_COMPONENT_BTN_XPATH = "%s//a[text()='Add a line']" % ACTIVE_TABLE_XPATH
COMPONENT_ROW = "%s//tbody/tr[contains(@class, 'o_selected_row')]" % ACTIVE_TABLE_XPATH
SUGGESTION_DROPDOWN = ".//ul[contains(@class, 'ui-menu') and contains(@style, 'top')]"
product_xpath = "./td[1]//input"
quantity_xpath = './/td[3]//input'
CONFIRM_BTN_XPATH = ".//button/span[contains(text(), 'Confirm')]"
MARK_AS_DONE_BTN_XPATH = ".//button/span[contains(text(), 'Mark as Done')]"
APPLY_BTN_XPATH = ".//button/span[contains(text(), 'Apply')]"
MODAL_DIALOG_XPATH = ".//div[contains(@class, 'modal-dialog')]"
STATUS_BAR_XPATH = ".//div[contains(@class, 'o_statusbar_status')]"
CURRENT_STATUS_XPATH = "%s/button[@title='Current state']" % STATUS_BAR_XPATH
COMPONENT_ROW_XPATH = "%s/tbody/tr[@class='o_data_row']" % ACTIVE_TABLE_XPATH

VERIFY_PRODUCT_NAME_XPATH = ".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//td[@name='product_id']"
VERIFY_PRODUCT_TO_CONSUME_XPATH=".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//span[@name='product_uom_qty']"
VERIFY_PRODUCT_CONSUMED_XPATH=".//div[@class='tab-pane active']//table//tbody//tr[@class='o_data_row']//td[@name='quantity_done']"

