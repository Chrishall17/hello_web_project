import re
from playwright.sync_api import Page, expect

"""
GET /books
"""
def test_get_books(db_connection, web_client): # Note web_client fixture, see conftest.py
    # We seed our database with the book store seed file
    db_connection.seed("seeds/book_store.sql")

    # We make a GET request to /books
    response = web_client.get("/books")

    # We assert that the response status code is 200
    assert response.status_code == 200

    # We assert that the response data is the same as the string we expect
    assert response.data.decode("utf-8") == "\n".join([
        "Book(1, Invisible Cities, Italo Calvino)",
        "Book(2, The Man Who Was Thursday, GK Chesterton)",
        "Book(3, Bluets, Maggie Nelson)",
        "Book(4, No Place on Earth, Christa Wolf)",
        "Book(5, Nevada, Imogen Binnie)"
    ])

"""
GET /books/<id>
"""
def test_get_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.get("/books/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)"

"""
POST /books
"""
def test_create_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.post("/books", data={
        "title": "The Great Gatsby",
        "author_name": "F. Scott Fitzgerald"
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book added successfully"

    response = web_client.get("/books")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Book(1, Invisible Cities, Italo Calvino)\n" +
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" +
        "Book(3, Bluets, Maggie Nelson)\n" +
        "Book(4, No Place on Earth, Christa Wolf)\n" +
        "Book(5, Nevada, Imogen Binnie)\n" +
        "Book(6, The Great Gatsby, F. Scott Fitzgerald)"
    ])

"""
DELETE /books/<id>
"""
def test_delete_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.delete("/books/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book deleted successfully"

    response = web_client.get("/books")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" +
        "Book(3, Bluets, Maggie Nelson)\n" +
        "Book(4, No Place on Earth, Christa Wolf)\n" +
        "Book(5, Nevada, Imogen Binnie)"
    ])

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))