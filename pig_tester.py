import pig_refactored as pr


def main():    
    print(pr.pig_latinize("hello"));
    print("First test passes: ", (pr.pig_latinize("hello") == "ellohay"));
    print(pr.pig_latinize("each"));
    print("Second test passes: ", (pr.pig_latinize("Each") == "Eachway"));
    print(pr.pig_latinize("PC"));
    print("Third test passes: ", (pr.pig_latinize("PC") == "PCAY"));

if __name__ == "__main__":
    main()
