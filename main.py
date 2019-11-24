import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

SEP = '/'


def _path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def organise(source_file, dest_root):
    ''' Take the source file and organise by artist/album '''
    source_mp3 = MP3File(source_file)

    artist_dir = source_mp3.artist
    album_dir = source_mp3.album

    print(artist_dir)
    print(album_dir)

    ' check if sub folder 1 exists and create as necessary '

    artist_album_dir = dest_root + SEP + artist_dir + SEP + album_dir
    
    if(os.path.isdir(artist_album_dir) == False):
        os.mkdir(artist_album_dir)
        
    ' check if sub folder 2 exists and create as necessary '

    fileName = _path_leaf(source_file)
    
    dest_mp3 = MP3File(artist_album_dir + SEP + filename)
    
    ' write file to dest_root/artist_dir/album_dir'
    dest_mp3.save()


    
source_file = sys.argv[0]
dest_root = sys.argv[1]

organise(source, dest_root)

    
    
