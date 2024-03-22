## avb@live.com
## https://github.com/aakth

import libvs as lv


result = lv.set_mvt_enhance(video_in, container_fps, display_fps)
if result is not None:
    result.set_output()

