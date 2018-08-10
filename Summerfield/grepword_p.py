def main():
    child = os.path.join(os.path.dirname(__file__), grepword_p_child.py)
    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    files_per_process = len(filelist) // opts.count
    start, end = 0, files_per_process + (len(filelist) % opts.count)
