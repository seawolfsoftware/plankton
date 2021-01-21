from searchtweets import ResultStream, gen_request_parameters, load_credentials


search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)


topic = val = input("Enter your topic: ")


# cashtags not supported as of 01/19/21
query = gen_request_parameters(topic, results_per_call=100)
print(query)


rs = ResultStream(request_parameters=query,
                max_results=500,
                max_pages=1,
                **search_args)

print(rs)

tweets = list(rs.stream())

# using unidecode to prevent emoji/accents printing
if tweets:
    [print(tweet) for tweet in tweets[0:10]]
else:
    print("No matching tweets")
