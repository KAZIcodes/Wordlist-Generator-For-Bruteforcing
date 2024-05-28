import argparse
from itertools import permutations, combinations

def read_words_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def parse_command_line():
    parser = argparse.ArgumentParser(description="Generate permutations and combinations of words.")
    parser.add_argument('-w', '--wordsfile', type=str, help="File containing words, one per line.")
    parser.add_argument('-p', '--permutations', type=str, help="Comma-separated words (spaces allowed).")
    parser.add_argument('-min', '--minlen', type=int, default=1, help="Minimum length of combinations.")
    parser.add_argument('-max', '--maxlen', type=int, help="Maximum length of combinations.")
    parser.add_argument('-o', '--output', type=str, help="Output file to save results.")
    parser.add_argument('-s', '--symbols', type=str, help="Symbols to insert into words.")
    parser.add_argument('--positions', type=str, help="Comma-separated list of positions to insert symbols (0-based).")
    
    return parser.parse_args()

def generate_combinations(words, min_len, max_len):
    all_combinations = []
    for i in range(min_len, max_len + 1):
        all_combinations.extend(combinations(words, i))

    all_permutations = []
    for combo in all_combinations:
        all_permutations.extend([''.join(p) for p in permutations(combo)])

    return all_permutations

def insert_symbols(word, symbols, positions):
    result = []
    for symbol in symbols:
        for pos in positions:
            result.append(word[:pos] + symbol + word[pos:])
    return result

def main():
    args = parse_command_line()

    if args.wordsfile:
        words = read_words_from_file(args.wordsfile)
    elif args.permutations:
        words = [word.strip() for word in args.permutations.split(',')]
    else:
        print("Either a words file (-w) or a comma-separated list of words (-p) must be provided.")
        return

    max_len = args.maxlen if args.maxlen else len(words)
    min_len = args.minlen

    if min_len > max_len:
        print("Minimum length cannot be greater than maximum length.")
        return

    all_permutations = generate_combinations(words, min_len, max_len)

    if args.symbols:
        symbols = list(args.symbols)
        if args.positions:
            positions = list(map(int, args.positions.split(',')))
        else:
            positions = list(range(len(words[0]) + 1))
            
        all_permutations_with_symbols = []
        for perm in all_permutations:
            perms_with_symbols = [perm]
            for word in perm.split():
                extended_words = insert_symbols(word, symbols, positions)
                new_perms = []
                for ew in extended_words:
                    for pws in perms_with_symbols:
                        new_perms.append(pws.replace(word, ew, 1))
                perms_with_symbols = new_perms
            all_permutations_with_symbols.extend(perms_with_symbols)
        all_permutations = all_permutations_with_symbols

    if args.output:
        with open(args.output, "w") as f:
            for perm in all_permutations:
                f.write(perm + "\n")
    else:
        for perm in all_permutations:
            print(perm)

if __name__ == "__main__":
    main()
