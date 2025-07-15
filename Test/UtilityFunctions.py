def find_el(by: str, element_identifier: str, search_method):
    try:
        return WebDriverWait(driver, 10).until(
            search_method((by, element_identifier))
        )
    except Exception as e:
        print(f"Exception detected:\n{e}")
        sys.exit()


def type_text(text: str, by: str, element_identifier: str, search_method):
    text_field = find_el(by, element_identifier, search_method)
    text_field.clear()
    text_field.send_keys(text)