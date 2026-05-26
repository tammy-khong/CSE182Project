import pandas as pd
import matplotlib.pyplot as plt

def dist_plot(file):
    amp_df = pd.read_csv(file)

    cdk12 = amp_df[amp_df['Oncogenes'].str.contains('CDK12', na = False)]
    cdk12 = cdk12[['Classification', 'Oncogenes']]
    
    print(cdk12)

    amp_freq = cdk12['Classification'].value_counts()
    
    amp_index = amp_freq.index.to_list()
    amp_vals = amp_freq.values
    plt.clf()

    if len(amp_index) == 0:
        amp_index = ["None"]
        amp_vals = [0]
    
    
    plt.bar(amp_index,amp_vals)
    plt.title(f"Distribution of Amplification Type {file}")
    plt.xlabel("Amplification Type")
    plt.ylabel("Count")
    plt.savefig(f"amp_type_{file}.png")


dist_plot("PCAWG_summary.csv")
dist_plot("Pediatric Pancancer_summary.csv")