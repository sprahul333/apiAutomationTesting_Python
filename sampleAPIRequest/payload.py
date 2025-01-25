def jsonPayload(bookname,isbnNumber,author):
    jsonData={
        "name": bookname,
        "isbn": isbnNumber,
        "aisle": "227",
        "author": author
    }

    return jsonData