"""Script for testing the whole of pyconfluence.

Requires environment variables PYCONFLUENCE_TEST_SPACE and
PYCONFLUENCE_TEST_PARENT_ID to be set accordingly.

PYCONFLUENCE_TEST_SPACE: the space you want the tests performed in.
PYCONFLUENCE_TEST_PARENT_ID: the ID of the parent page you want to test under.
"""

import pyconfluence as pyco
import os

def run():
    """Commence testing!"""

    # Check if variables are present
    if (not os.environ.get("PYCONFLUENCE_TEST_SPACE") or
            not os.environ.get("PYCONFLUENCE_TEST_PARENT_ID")):
        print ("One or more testing environment variables are not set.")

    space = os.environ["PYCONFLUENCE_TEST_SPACE"]
    parent_id = os.environ["PYCONFLUENCE_TEST_PARENT_ID"]

    content = ("\"I, for one, welcome our new bot overlords.\"<br/>Testing in "
               "progress for Pyconfluence.")

    print ("Creating page \"Pyconfluence Testing\"...")
    pyco.create_page("Pyconfluence Testing", parent_id, space, content)

    if pyco.page_exists("Pyconfluence Testing", space):
        print ("Getting page ID and name...")
        page_id = pyco.get_page_id("Pyconfluence Testing", space)
        page_name = pyco.get_page_name(page_id)

        print ("Page ID: " + page_id)
        print ("Page name: " + page_name)
    else:
        print ("This error should not be encountered. If you\'re reading this, "
               "well done! You have failed spectacularly. Incoming crash...")

    print ("Getting page data list #1: ")
    print (pyco.get_page_full(page_id))

    print ("Getting page data list #2: ")
    print (pyco.get_page_full_more(page_name, space))

    print ("Getting page content: ")
    print (pyco.get_page_content(page_id))

    child_content = ("I am a child page! Look at me!")

    print ("Creating child page uno...")
    pyco.create_page("Child page uno", page_id, space, child_content)

    print ("Creating child page dos...")
    pyco.create_page("Child page dos", page_id, space, child_content)

    print ("Here are the children belonging to " + page_name + ": ")
    print (pyco.get_page_children(page_id))

    print ("Deleting child page dos...")
    pyco.delete_page(pyco.get_page_id("Child page dos", space))

    print ("Deleting " + page_name + " and the other child page.")
    pyco.delete_page_full(page_id)

    print ("\n\nJob\'s done.")


if __name__ == "__main__":
    run()
