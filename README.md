# CircadianAnnotalo
Ez egy annotáló script ahhoz, hogy egy megadott dav fájlt 1 másodperces szakaszonként felannotáljunk a NIDCAP szerinti fázisokat tekintve. Az adott 1 perces szakasz a következő fázisok valamelyikével jellemezhető: ["Csendes-Alvas", "Aktiv-Alas", "Atmeneti", "Csendes-Eber", "Aktiv-Eber", "Siras"].

Hogyan használd? 

Az elején meg kell adni a file_name-nek, hogy milyen dav fájlon fusson. Ha valahol máshol van a gépen és nem a gyökérben akkor meg kell adni a helyét is, ahogy a példában nálam most a "NVR_ch2_main_20230818123500_20230818124000.dav" fájl a "/media/nas/PUBLIC/Circadian_PIC_Videos/videos/60AA/" helyen volt található.

Minden egy perc után feljön egy panel ahol kiválaszthatjuk az aktuális előtte lejátszott 1 másodperces szakaszra igaz NIDCAP fázist.

Az annotáció eredménye az lesz, hogy létrejön egy a dav fájl nevével azonos nevű txt fájl amiben a panelen megadott annotációk lesznek. Pont annyi számnak kell benne létrejönnie, mint amennyi a frame van a feldolgozott dav fájlban.
