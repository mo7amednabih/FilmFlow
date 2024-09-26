import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

pd.set_option("display.max_columns" , None)
df=pd.read_csv("tmdb-movies.csv")

# print(df.head())
# print(df.describe())
# print(df.nunique())
# print(df.describe(include="object").T)



def plot_top_directors(df, top_n=10):

    directors_count = df["director"].value_counts().head(top_n)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(directors_count.index, directors_count.values)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), 
                 ha='center', va='bottom', fontsize=10)

    plt.xlabel("Director")
    plt.ylabel("Number of Films")
    plt.title(f"Top {top_n} Directors by Number of Films")
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()


def plot_top_directors_by_budget_and_revenue(df, top_n=10):
   
    top_directors = df.groupby("director")[["budget", "revenue"]].sum().sort_values("revenue", ascending=False).head(top_n)
    
    top_directors.plot(kind='bar', figsize=(12, 8))
    

    plt.xlabel("Director")
    plt.ylabel("Amount")
    plt.title(f"Top {top_n} Directors by Budget and Revenue")
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()  # لضمان عدم قص النص
    plt.show()
    


    
def plot_top_film_by_budget_and_revenue(df, top_n=10):
    top_film = df.groupby("original_title")[["budget_adj", "revenue_adj"]].sum().sort_values("budget_adj", ascending=False).head(10)

    top_film.plot(kind='bar', figsize=(12, 8))

    plt.xticks(rotation=45, ha='right')  


    plt.xlabel("Film")
    plt.ylabel("Amount")
    plt.title(f"Top {top_n} Films by Budget and Revenue")
    
    plt.tight_layout()  # لضمان عدم قص النص
    plt.show()
    
def plot_Top_production_companies(df):

    all_companies = df['production_companies'].dropna().str.split('|').explode()
    company_counts = all_companies.value_counts().head(10)

    company_counts.plot(kind='bar', figsize=(12, 8))

    plt.xlabel("Production Company")
    plt.ylabel("Number of Films")
    plt.title("Top 10 Production Companies by Number of Films")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def plot_top_actors(df):
    all_actors = df['cast'].dropna().str.split('|').explode()

    actor_counts = all_actors.value_counts().head(10)

    actor_counts.plot(kind='bar', figsize=(12, 8))

    plt.xlabel("Actor")
    plt.ylabel("Number of Films")
    plt.title("Top 10 Actors by Number of Films")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def plot_popular_films(df):    
    
    top_10_popular_films = df[['original_title', 'popularity', 'revenue']].sort_values('popularity', ascending=False).head(10)

    plt.figure(figsize=(12, 8))

    bars = plt.barh(top_10_popular_films['original_title'], top_10_popular_films['revenue'])

    for bar, popularity in zip(bars, top_10_popular_films['popularity']):
        plt.text(bar.get_width() + 5000000, bar.get_y() + bar.get_height() / 2, f'{popularity:.2f}', 
                va='center', ha='left', color='black', fontsize=10)

    plt.xlabel("Revenue")
    plt.ylabel("Film Title")
    plt.title("Revenue and Popularity of Top 10 Most Popular Films")

    plt.tight_layout()
    plt.show()
    
def plot_Film_from_2015_to_2005(df):
    
    start_year = 2005
    end_year = 2015

    df_filtered = df[(df['release_year'] >= start_year) & (df['release_year'] <= end_year)]

    films_per_year = df_filtered['release_year'].value_counts().sort_values(ascending=False)

    films_per_year.plot(kind='bar', figsize=(12, 8))

    plt.xlabel("Year")
    plt.ylabel("Number of Films")
    plt.title("Number of Films Released Each Year from 2005 to 2015")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    

    
def plot_top_genres(df):
    all_genres = df['genres'].dropna().str.split('|').explode()

    genre_counts = all_genres.value_counts()


    genre_counts.plot(kind='bar', figsize=(12, 6))

    plt.xlabel("Genre")
    plt.ylabel("Number of Films")
    plt.title("Top Genres Represented in Films")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
  

   
def plot_Total_Revenue(df):
    df['genres'] = df['genres'].fillna('')
    all_genres = df[['genres', 'revenue']].copy()
    all_genres['genres'] = all_genres['genres'].str.split('|')

    all_genres = all_genres.explode('genres')

    genre_revenue = all_genres.groupby('genres')['revenue'].sum().sort_values(ascending=False)

    genre_revenue.plot(kind='bar', figsize=(12, 6))

    plt.xlabel("Genre")
    plt.ylabel("Total Revenue")
    plt.title("Total Revenue by Genre")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def plot_corr(df):
    plt.figure(figsize=(12, 10))

    sns.heatmap(df.corr(numeric_only= True),annot=True)
    plt.title("Correlation Heatmap")
    plt.show()
    
def dashboard_director(df, top_n=10):
    fig, axs = plt.subplots(1, 2, figsize=(18, 8)) 

    directors_count = df["director"].value_counts().head(top_n)
    bars = axs[0].bar(directors_count.index, directors_count.values)

    for bar in bars:
        height = bar.get_height()
        axs[0].text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), 
                    ha='center', va='bottom', fontsize=10)

    axs[0].set_xlabel("Director")
    axs[0].set_ylabel("Number of Films")
    axs[0].set_title(f"Top {top_n} Directors by Number of Films")
    axs[0].tick_params(axis='x', rotation=45)

    top_directors = df.groupby("director")[["budget", "revenue"]].sum().sort_values("revenue", ascending=False).head(top_n)
    
    top_directors.plot(kind='bar', ax=axs[1])  

    axs[1].set_xlabel("Director")
    axs[1].set_ylabel("Amount")
    axs[1].set_title(f"Top {top_n} Directors by Budget and Revenue")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
    
def dashboard_Film(df, top_n=4):
    fig, axs = plt.subplots(2, 2, figsize=(30, 20))  
    
    # Top 10 Films by Budget and Revenue
    top_film = df.groupby("original_title")[["budget_adj", "revenue_adj"]].sum().sort_values("budget_adj", ascending=False).head(top_n)
    top_film.plot(kind='bar', ax=axs[0, 0])
    axs[0, 0].set_title(f"Top {top_n} Films by Budget and Revenue")
    axs[0, 0].set_xlabel("Film")
    axs[0, 0].set_ylabel("Amount")
    axs[0, 0].tick_params(axis='x', rotation=45, labelsize=10)

    # Top 10 Production Companies by Number of Films
    all_companies = df['production_companies'].dropna().str.split('|').explode()
    company_counts = all_companies.value_counts().head(top_n)
    company_counts.plot(kind='bar', ax=axs[0, 1])
    axs[0, 1].set_title("Top 10 Production Companies by Number of Films")
    axs[0, 1].set_xlabel("Production Company")
    axs[0, 1].set_ylabel("Number of Films")
    axs[0, 1].tick_params(axis='x', rotation=45)

    # Top 10 Actors by Number of Films
    all_actors = df['cast'].dropna().str.split('|').explode()
    actor_counts = all_actors.value_counts().head(top_n)
    actor_counts.plot(kind='bar', ax=axs[1, 0])
    axs[1, 0].set_title("Top 10 Actors by Number of Films")
    axs[1, 0].set_xlabel("Actor")
    axs[1, 0].set_ylabel("Number of Films")
    axs[1, 0].tick_params(axis='x', rotation=45)

    # Revenue and Popularity of Top 10 Most Popular Films
    top_10_popular_films = df[['original_title', 'popularity', 'revenue']].sort_values('popularity', ascending=False).head(top_n)
    bars = axs[1, 1].barh(top_10_popular_films['original_title'], top_10_popular_films['revenue'])
    
    for bar, popularity in zip(bars, top_10_popular_films['popularity']):
        axs[1, 1].text(bar.get_width() + 5000000, bar.get_y() + bar.get_height() / 2, f'{popularity:.2f}', 
                       va='center', ha='left', color='black', fontsize=10)

    axs[1, 1].set_title("Revenue and Popularity of Top 10 Most Popular Films")
    axs[1, 1].set_xlabel("Revenue")
    axs[1, 1].set_ylabel("Film Title")

    plt.tight_layout()
    plt.show()

def dashboard_genres_revenue(df):
    fig, axs = plt.subplots(1, 2, figsize=(20, 6))  
    
    # Top Genres Represented in Films
    all_genres = df['genres'].dropna().str.split('|').explode()
    genre_counts = all_genres.value_counts()
    genre_counts.plot(kind='bar', ax=axs[0])
    axs[0].set_title("Top Genres Represented in Films")
    axs[0].set_xlabel("Genre")
    axs[0].set_ylabel("Number of Films")
    axs[0].tick_params(axis='x', rotation=45)
    
    # Total Revenue by Genre
    df['genres'] = df['genres'].fillna('')
    all_genres_rev = df[['genres', 'revenue']].copy()
    all_genres_rev['genres'] = all_genres_rev['genres'].str.split('|')
    all_genres_rev = all_genres_rev.explode('genres')
    genre_revenue = all_genres_rev.groupby('genres')['revenue'].sum().sort_values(ascending=False)
    genre_revenue.plot(kind='bar', ax=axs[1])
    axs[1].set_title("Total Revenue by Genre")
    axs[1].set_xlabel("Genre")
    axs[1].set_ylabel("Total Revenue")
    axs[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()





def main():
    while True:
        user_input = input("Do you want to see:\n1. Top directors by number of films\n2. Top directors by budget and revenue \n3. Top films by budget and revenue \n4. Top 10 Production Companies by Number of Films \n5. Number of Films Released Each Year from 2005 to 2015\n6. Top 10 Actors by Number of Films\n7. Top Genres Represented in Films\n8. Revenue and Popularity of Top 10 Most Popular Films\n9. Total Revenue by Genre\n10. Correlation Heatmap\n11. dashboard of director\n12. dashboard_Film\n13. dashboard_genres\n14. Don't need any thing\nEnter any num you need: ").strip()
        if user_input == '1':
            plot_top_directors(df, top_n=10)
        elif user_input == '2':
            plot_top_directors_by_budget_and_revenue(df, top_n=10)
        elif user_input == '3':
            plot_top_film_by_budget_and_revenue(df, top_n=10)
        elif user_input == '4':
            plot_Top_production_companies(df)
        elif user_input == '5':
            plot_Film_from_2015_to_2005(df)
        elif user_input == '6':
             plot_top_actors(df)
        elif user_input == '7':
            plot_top_genres(df)
        elif user_input == '8':
            plot_popular_films(df)
        elif user_input == '9':
            plot_Total_Revenue(df)
        elif user_input == '10':
            plot_corr(df)
        elif user_input == '11':
            dashboard_director(df, top_n=10)
        elif user_input == '12':
            dashboard_Film(df)
        elif user_input == '13':
            dashboard_genres_revenue(df)
        elif user_input == '14':
            break
        else:
            print("Invalid input. Please enter 1 to 14.")


main()



























# # Top 10 Runtime vs. Average Vote
# top_film = df.groupby("runtime")[["vote_average"]].mean().sort_values("vote_average", ascending=False).head(10)

# top_film.plot(kind='bar')

# plt.xticks(rotation=45, ha='right')  

# # إضافة العنوان والتسميات للمحور
# plt.xlabel("Runtime (minutes)")
# plt.ylabel("Average Vote")
# plt.title("Top 10 Runtime vs. Average Vote")

# # عرض الرسم
# plt.tight_layout()  # لضمان عدم قص النص
# plt.show()