from pypdf import PdfWriter

merger = PdfWriter()

try:
    count = int(input("How many PDFs do you want to merge? "))
    if count < 2:
        print("Please enter at least 2 PDFs.")
    else:
        for i in range(count):
            filename = input(f"Enter PDF {i + 1} filename: ").strip().strip('"')
            merger.append(filename)

        with open("merged.pdf", "xb") as output:
            merger.write(output)

        print("Success! Your PDFs are merged into merged.pdf.")

except FileNotFoundError:
    print("PDF not found. Check the filename or enter its full path.")
except FileExistsError:
    print("merged.pdf already exists. Rename it before running again.")
except ValueError:
    print("Please enter a valid number.")
except Exception as error:
    print("Could not merge PDFs:", error)
finally:
    merger.close()
