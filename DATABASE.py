import mysql.connector

class Database:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "Dictionary"
        )
        except Exception as err:
            print(err)

        else:
            print("Database ga ulandi!")



# Database ga ma'lumot qo'shish
    def insert_new_word(self,eng_word,uzb_word):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    INSERT INTO dictionary(ENGLISH,UZBEK) VALUES(
                    "{eng_word}",
                    "{uzb_word}"
                    );
                    """
                cursor.execute(sql)
                self.connection.commit()

        except Exception as err:
            print(err)


        else:
            return "SAQLANDI"
        
        

# Database degi hamma ma'lumotlani olish
    def get_all_words(self):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    SELECT * 
                    FROM dictionary;
                """
                cursor.execute(sql)
                data = cursor.fetchall()


        except Exception as err:
            print(err)
        

        else:
            return data
        

#qidirilyapkan so'zni DATABASE dan olish
    def searched_word(self,word):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""
                    SELECT ENGLISH,UZBEK
                    FROM dictionary
                    WHERE  ENGLISH LIKE "{word}"
                    OR UZBEK LIKE "{word}";
                """
                cursor.execute(sql)
                words = cursor.fetchall()

        except Exception as err:
            print(err)
        

        else:
            if words[0][0] != word:
                return words[0][0]
            else:
                return words[0][1]
               
                       

