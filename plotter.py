import data_processor as dp

def get_command_line_args():
    parser = argparse.ArgumentParser(description = "dunno what this does yet")
    parser.add_argument("--x",
                        type = int, 
                        help = "number of rows in the matrix'")
    parser.add_argument("--y",
                        type = int,
                        help = "number of columns in the matrix")

    return parser.parse_args()


def main():
    args = get_command_line_args()
    print(dp.get_random_matrix(args.x, args.y))
    
if __name__ == '__main__':
    main()