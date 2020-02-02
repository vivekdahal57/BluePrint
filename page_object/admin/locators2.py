from selenium.webdriver.common.by import By


class AdminCollectionsListPageLocator:
    collection_title_text = (By.XPATH, "//h1[contains(text(),'Select collection to change')]")
    collection_add_button = (By.XPATH, "//a[@class='addlink']")
    collection_change_success = (By.CSS_SELECTOR, "li.success")
    collection_search_field = (By.ID, "searchbar")
    collection_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    collection_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self):
        pass


class AdminAddCollectionPageLocator:
    add_collection_title_text = (By.XPATH, "//h1[contains(text(),'Add collection')]")
    add_collection_change_collection_title_text = (By.XPATH, "//h1[contains(text(),'Change collection')]")
    add_collection_save_button = (By.NAME, "_save")
    add_collection_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self):
        pass
