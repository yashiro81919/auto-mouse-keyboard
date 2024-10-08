import sqlite3

DB_FILE='D:/game/PES6FLS/backup/pes-18-more.db'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# validation nation for all teams
cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='england' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('E1', 'E2') and row[0] != 11:
        print(row[1] + ' should have 11 england players')
    elif row[1] not in ('Z', 'N', 'E1', 'E2') and row[0] > 2:
        print(row[1] + ' should have less than 3 england players')
    elif row[1] not in ('Z', 'N', 'E1', 'E2') and row[0] < 1:
        print(row[1] + ' should have at least 1 england player')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='spain' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('S1', 'S2') and row[0] != 11:
        print(row[1] + ' should have 11 spain players')
    elif row[1] not in ('Z', 'N', 'S1', 'S2') and row[0] > 2:
        print(row[1] + ' should have less than 3 spain players')
    elif row[1] not in ('Z', 'N', 'S1', 'S2') and row[0] < 1:
        print(row[1] + ' should have at least 1 spain player')        


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='italy' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('I1', 'I2') and row[0] != 11:
        print(row[1] + ' should have 11 italy players')
    elif row[1] not in ('Z', 'N', 'I1', 'I2') and row[0] > 2:
        print(row[1] + ' should have less than 3 italy players')
    elif row[1] not in ('Z', 'N', 'I1', 'I2') and row[0] < 1:
        print(row[1] + ' should have at least 1 italy player')    


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='france' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('F1', 'F2') and row[0] != 11:
        print(row[1] + ' should have 11 france players')
    elif row[1] not in ('Z', 'N', 'F1', 'F2') and row[0] > 2:
        print(row[1] + ' should have less than 3 france players')
    elif row[1] not in ('Z', 'N', 'F1', 'F2') and row[0] < 1:
        print(row[1] + ' should have at least 1 france player')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='netherlands' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('N1', 'N2') and row[0] != 11:
        print(row[1] + ' should have 11 netherlands players')
    elif row[1] not in ('Z', 'N', 'N1', 'N2') and row[0] > 1:
        print(row[1] + ' should have less than 2 netherlands players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='germany' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('G1', 'G2') and row[0] != 11:
        print(row[1] + ' should have 11 germany players')
    elif row[1] not in ('Z', 'N', 'G1', 'G2') and row[0] > 1:
        print(row[1] + ' should have less than 2 germany players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='brazil' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('B1') and row[0] != 11:
        print(row[1] + ' should have 11 brazil players')
    elif row[1] in ('A1') and row[0] > 0:
        print(row[1] + ' should have no any brazil player')        
    elif row[1] not in ('Z', 'N', 'B1') and row[0] > 2:
        print(row[1] + ' should have less than 3 brazil players')
    elif row[1] not in ('Z', 'N', 'B1', 'A1') and row[0] < 1:
        print(row[1] + ' should have at least 1 brazil player')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='portugal' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('P1') and row[0] != 11:
        print(row[1] + ' should have 11 portugal players')
    elif row[1] not in ('Z', 'N', 'P1') and row[0] > 1:
        print(row[1] + ' should have less than 2 portugal players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='argentina' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('A1') and row[0] != 11:
        print(row[1] + ' should have 11 argentina players')
    elif row[1] in ('B1') and row[0] > 0:
        print(row[1] + ' should have no any argentina player')           
    elif row[1] not in ('Z', 'N', 'A1') and row[0] > 1:
        print(row[1] + ' should have less than 2 argentina players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='czech' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('C1') and row[0] != 11:
        print(row[1] + ' should have 11 czech players')
    elif row[1] not in ('Z', 'N', 'C1') and row[0] > 1:
        print(row[1] + ' should have less than 2 czech players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='korea' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('K1') and row[0] != 11:
        print(row[1] + ' should have 11 korea players')
    elif row[1] in ('J1') and row[0] > 0:
        print(row[1] + ' should have no any korea player')        
    elif row[1] not in ('Z', 'N', 'K1') and row[0] > 1:
        print(row[1] + ' should have less than 2 korea players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='japan' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('J1') and row[0] != 11:
        print(row[1] + ' should have 11 japan players')
    elif row[1] in ('K1') and row[0] > 0:
        print(row[1] + ' should have no any japan player')        
    elif row[1] not in ('Z', 'N', 'J1') and row[0] > 1:
        print(row[1] + ' should have less than 2 japan players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation in ('south africa', 'senegal', 'nigeria', 'ghana', 'egypt', 'cote', 'cameroon', 'leone', 'algeria') group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] in ('F1', 'F2') and row[0] != 2:
        print(row[1] + ' should have 2 african players')
    elif row[1] not in ('Z', 'N', 'F1', 'F2') and row[0] > 1:
        print(row[1] + ' should have less than 2 african players')


cursor.execute("select count(*), club, nation from t_player where nation in ('south africa', 'senegal', 'nigeria', 'ghana', 'egypt', 'cote', 'cameroon', 'leone', 'algeria', 'ireland', 'denmark', 'turkey', 'croatia', 'usa', 'poland', 'romania', 'serbia', 'australia', 'norway') group by club, nation")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] > 1:
        print(row[1] + ' should have less than 2 ' + row[2] + ' players')


cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where nation='sweden' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] > 2:
        print(row[1] + ' should have less than 3 sweden players')
    elif row[1] not in ('Z', 'N') and row[0] < 1:
        print(row[1] + ' should have at least 1 sweden player')     


# validate number of total players
cursor.execute("select club, count(*) from t_player group by club")
rows = cursor.fetchall()

for row in rows:
    if row[0] not in ('Z', 'N') and row[1] != 26:
        print(row[0] + ' should have 26 players')

# validate C level players
cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where level = 'C' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] not in (4, 5):
        print(row[1] + ' should have 4 or 5 level C players')

# validate C injury players
cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where injury = 'C' group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] > 2:
        print(row[1] + ' should have less than 3 injury C players')
    elif row[1] not in ('Z', 'N') and row[0] < 1:
        print(row[1] + ' should have at least 1 injury C player')

# validate A level players
cursor.execute("select ifnull(b.num, 0), a.club from (select club from t_player group by club) a left join (select count(*) num, club from t_player where level = 'A' and role not in ('GK') group by club) b on a.club = b.club")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] != 10:
        print(row[1] + ' should have 10 level A players')

# validate L R SM players
cursor.execute("select count(*), club, side from t_player where side in ('L', 'R') and role in ('SM') group by club, side")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] > 2:
        print(row[1] + ' should have less than 3 ' + row[2] + ' SM players')

# validate L R DF SB players
cursor.execute("select count(*), club, side from t_player where side in ('L', 'R') and role in ('DF', 'SB') group by club, side")
rows = cursor.fetchall()

for row in rows:
    if row[1] not in ('Z', 'N') and row[0] > 3:
        print(row[1] + ' should have less than 4 ' + row[2] + ' DF or SB players')


conn.close()