import argparse

def cmd_update(args):
    print("update: not implemented yet")
    
def cmd_list(args):
    print("list: not implemented yet")
    
def cmd_add(args):
    print(f"add: not implemented yet, but url passed is: {args.url}")
    
def cmd_remove(args):
    print(f"remove: not implemented yet, but url passed is: {args.url}")
    
def cmd_sources(args):
    print("sources: not implemented yet")

def main():
    parser = argparse.ArgumentParser(prog="jobdiff", description="Track new job postings.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    #parser setup for "update" command, complete with help message 
    update_parser = subparsers.add_parser("update", help="fetch new postings from all sources")
    update_parser.set_defaults(func=cmd_update)
    
    #parser setup for "list" command, complete with help message
    list_parser = subparsers.add_parser("list", help="prints list of currently active job postings from provided sources")
    list_parser.set_defaults(func=cmd_list)
    
    #parser setup for "add" command, complete with help message and argument
    add_parser = subparsers.add_parser("add", help="adds provided url to list of sources to pull postings from")
    add_parser.add_argument("url", help="url linking to site that will be added to list of sources") #adding required "url" argument to "add" command
    add_parser.set_defaults(func=cmd_add)
    
    #parser setup for "remove" command, complete with help message and argument
    remove_parser = subparsers.add_parser("remove", help="removes provided url from list of sources if present in current list")
    remove_parser.add_argument("url", help="url to be removed from source list") #adding required "url" argument to "remove" command
    remove_parser.set_defaults(func=cmd_remove)
    
    #parser setup for "sources" command, complete with help message
    sources_parser = subparsers.add_parser("sources", help="prints currently stored list of sources provided by user")
    sources_parser.set_defaults(func=cmd_sources)
    
    args = parser.parse_args()
    args.func(args)