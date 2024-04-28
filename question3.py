import text_utils as tu

def main():
    original_string = "hello world"
    reversed_string = tu.reverse_string(original_string)
    print("Original string:", original_string)
    print("Reversed string:", reversed_string)

    capitalized_string = tu.capitalize_string(original_string)
    print("Capitalized string:", capitalized_string)

if __name__ == "__main__":
    main()
