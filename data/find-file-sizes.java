import java.io.*;
import java.net.*;

class findFileSizes {
  public static int getFileSizeInBytes(String[] urlArray){
    for (String urlPath : urlArray) {
      String path = urlPath;
      try {
              URL url = new URL(path);
              URLConnection urlConnection = url.openConnection();
              urlConnection.connect();
              int file_size = urlConnection.getContentLength();
              System.out.println(url + " " + file_size);

          } catch (MalformedURLException e) {
            System.out.println(e);
            return -1;
          }catch (IOException e){
            System.out.println(e);
            return -1;
          }
    }
    return 1;
  }

  public static void main(String[] args) {
    String[] urls = {"https://database.lichess.org/lichess_db_standard_rated_2017-08.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-07.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-06.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-05.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-04.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-03.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-02.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2017-01.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-12.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-11.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-10.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-09.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-08.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-07.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-06.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-05.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-04.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-03.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-02.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2016-01.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-12.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-11.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-10.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-09.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-08.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-07.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-06.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-05.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-04.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-03.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-02.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2015-01.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-12.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-11.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-10.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-09.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-08.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-07.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-06.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-05.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-04.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-03.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-02.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2014-01.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-12.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-11.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-10.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-09.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-08.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-07.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-06.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-05.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-04.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-03.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-02.pgn.bz2",
   "https://database.lichess.org/lichess_db_standard_rated_2013-01.pgn.bz2"};

    getFileSizeInBytes(urls);
  }
}
