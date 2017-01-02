from toshokan import db
from toshokan.series.models import Series, Volume, Chapter, Doujinshi

db.create_all()
db.session.commit()

# series = [
#     Series("Dead Tube"),
#     Series("Gokukoku no Brynhildr"),
#     Series("Kabe ni Mary.com"),
#     Series("Boku no Futatsu no Tsubasa"),
#     Series("Earth Girls"),
#     Series("Ever Green"),
#     Series("Himitsu no Akuma-chan"),
#     Series("Idol Pretender"),
#     Series("Koe de Oshigoto!"),
#     Series("Koharu no Hibi"),
#     Series("Mayo Chiki!"),
#     Series("Mirai Nikki"),
#     Series("Nozoki Ana"),
#     Series("Onanie Master Kurosawa"),
#     Series("Akame ga Kill!"),
#     Series("Asuka Hybrid"),
#     Series("1/2 Prince"),
#     Series("Berserk"),
#     Series("Boku Girl"),
#     Series("Citrus"),
#     Series("D.Gray-man"),
#     Series("Eden no Ori"),
#     Series("Fairy Tail"),
#     Series("Green Worldz"),
#     Series("Jisatsutou"),
#     Series("Joshi Shouakusei Hajimemashita P!"),
#     Series("One Piece"),
#     Series("Pupa"),
#     Series("Rosario to Vampire: Season II"),
#     Series("Sekai no Hate de Aimashou"),
#     Series("Shingeki no Kyojin"),
#     Series("Sundome"),
#     Series("Suzumiya Haruhi no Yuutsu"),
#     Series("Uwa-Koi"),
#     Series("Yamada-kun to 7-nin no Majo"),
#     Series("Aku no Hana"),
#     Series("Ao Haru Ride"),
#     Series("Boku wa Mari no Naka"),
#     Series("Bokura no Hentai"),
#     Series("Gisou Honey Trap"),
#     Series("Hibi Chouchou"),
#     Series("Himouto! Umaru-chan"),
#     Series("Liar Game"),
#     Series("Masamune-kun no Revenge"),
#     Series("Megu♥Milk"),
#     Series("Nyotai-ka."),
#     Series("Pokemon Specials"),
#     Series("Tenshi na Konamaiki"),
#     Series("Tonari no Kashiwagi-san"),
#     Series("Tripeace"),
#     Series("Tsukiyo no Fromage"),
#     Series("Air Gear"),
#     Series("Akkan Baby"),
#     Series("Boku wa Ohimesama ni Narenai"),
#     Series("Gyo: Ugomeku Bukimi"),
#     Series("Okasubekarazu!! Junketsu Tokku!"),
#     Series("Oretama"),
#     Series("Tate no Yuusha no Nariagari"),
#     Series("Yuru Yuri")
# ]
#
# for s in series:
#     v = Volume(None, 1)
#     c = Chapter(None, 1)
#     d = Doujinshi("Test Doujin", artist="Lolita-Channel")
#
#     v.chapters.append(c)
#     s.volumes.append(v)
#     s.doujins.append(d)
#
#     db.session.add(s)
#
# db.session.commit()
