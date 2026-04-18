import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistics_system.settings')
django.setup()

from core.models import BlogPost

def update_blog_images():
    # Map specific slugs to generated images
    mappings = {
        "the-future-of-global-logistics-in-2026": "blog_1.png",
        "5-tips-for-faster-international-shipping": "blog_2.png",
    }
    
    for slug, img_name in mappings.items():
        try:
            post = BlogPost.objects.get(slug=slug)
            # We don't need to manually move the file into the upload_to path for this demo 
            # if we just reference the path or set it correctly.
            # But let's just use the /media/ path directly in the template if image field is empty.
            # For this demo, let's just update the image field string.
            post.image = f"blog/{img_name}" # This assumes it's in media/blog/
            post.save()
            print(f"Updated image for: {slug}")
        except BlogPost.DoesNotExist:
            pass

if __name__ == '__main__':
    # Ensure media/blog directory exists
    if not os.path.exists('media/blog'):
        os.makedirs('media/blog')
    
    # Move files to media/blog/
    import shutil
    if os.path.exists('media/blog_1.png'):
        shutil.move('media/blog_1.png', 'media/blog/blog_1.png')
    if os.path.exists('media/blog_2.png'):
        shutil.move('media/blog_2.png', 'media/blog/blog_2.png')
        
    update_blog_images()
