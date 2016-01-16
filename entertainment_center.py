import media
import fresh_tomatoes
import tmdb_query as tmdb


tangled = media.Movie(tmdb.tangled.title,
                      tmdb.tangled.description,
                      "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
                      "https://www.youtube.com/watch?v=JYKpIr1lSG0",
                      tmdb.tangled.release_date,
                      tmdb.tangled.tag_line)

avatar = media.Movie(tmdb.avatar.title,
                     tmdb.avatar.description,
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     tmdb.avatar.release_date,
                     tmdb.avatar.tag_line)

lebowski = media.Movie(tmdb.lebowski.title,
                       tmdb.lebowski.description,
                       "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                       tmdb.lebowski.release_date,
                       tmdb.lebowski.tag_line)

star_trek_first_contact = media.Movie(tmdb.first_contact.title,
                                      tmdb.first_contact.description,
                                      "https://upload.wikimedia.org/wikipedia/en/d/dd/Star_Trek_08-poster.png",
                                      "https://www.youtube.com/watch?v=7W-Fwgirzqw",
                                      tmdb.first_contact.release_date,
                                      tmdb.first_contact.tag_line)

transformers_live_action = media.Movie(tmdb.transformers.title,
                                       tmdb.transformers.description,
                                       "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                                       "https://www.youtube.com/watch?v=gAjgXlvVexI",
                                       tmdb.transformers.release_date,
                                       tmdb.transformers.tag_line)

bolt = media.Movie(tmdb.bolt.title,
                   tmdb.bolt.description,
                   "https://upload.wikimedia.org/wikipedia/en/4/44/Bolt_ver2.jpg",
                   "https://www.youtube.com/watch?v=s2-zHK4O-MQ",
                   tmdb.bolt.release_date,
                   tmdb.bolt.tag_line)

movies = [tangled,
          avatar,
          lebowski,
          star_trek_first_contact,
          transformers_live_action,
          bolt]
fresh_tomatoes.open_movies_page(movies)