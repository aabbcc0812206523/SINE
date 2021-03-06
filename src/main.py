from sine import SINETrainer
from parser import parameter_parser
from utils import read_graph, read_features, tab_printer

def main():
    """
    Parsing command lines, creating target matrix, fitting SINE and saving the embedding.
    """
    args = parameter_parser()
    tab_printer(args)
    model = SINETrainer(args)
    model.fit()
    model.save_embedding()

if __name__ =="__main__":
    main()
