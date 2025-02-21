import streamlit as st
from PIL import Image
import io
import base64
import zipfile
import os
from datetime import datetime

class StreamlitImageSlicer:
    def __init__(self):
        st.set_page_config(page_title="Image Grid Slicer", layout="wide")
        
        # Initialize session state
        if 'y_offset' not in st.session_state:
            st.session_state.y_offset = 0
        if 'processed_image' not in st.session_state:
            st.session_state.processed_image = None
        if 'final_image' not in st.session_state:
            st.session_state.final_image = None
        if 'bg_color' not in st.session_state:
            st.session_state.bg_color = 'black'

    def create_ui(self):
        st.title("Image Grid Slicer")
        
        with st.sidebar:
            uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
            grid_type = st.selectbox("Grid Type:", ["1x3", "2x3", "3x3"])
            bg_color = st.selectbox("Background Color:", ["black", "white"])

        if uploaded_file is not None:
            # Process image when uploaded or when grid type changes
            if ('last_upload' not in st.session_state or 
                st.session_state.last_upload != uploaded_file or
                'last_grid_type' not in st.session_state or 
                st.session_state.last_grid_type != grid_type):
                
                self.process_image(uploaded_file, bg_color, grid_type)
                st.session_state.last_upload = uploaded_file
                st.session_state.last_grid_type = grid_type
                st.session_state.grid_type = grid_type

            # Display preview
            if st.session_state.final_image:
                preview_img = self.add_guidelines(st.session_state.final_image.copy())
                st.image(preview_img, use_container_width=True)

                # Get max offset that prevents background exposure
                max_offset = max(1, st.session_state.max_offset)  # Ensure at least 1px difference
                
                # Add vertical position slider with capped range
                y_offset = st.slider(
                    "Adjust Vertical Position",
                    min_value=-max_offset,
                    max_value=max_offset,
                    value=st.session_state.y_offset
                )
                
                if y_offset != st.session_state.y_offset:
                    st.session_state.y_offset = y_offset
                    self.adjust_image_position(y_offset, grid_type)
                    st.rerun()

                # Initialize session state for showing download buttons
                if 'show_download_buttons' not in st.session_state:
                    st.session_state.show_download_buttons = False

                # Single slice button
                if st.button("Slice Image", key="slice_button"):
                    st.session_state.show_download_buttons = True
                    st.rerun()

                # Show download buttons if slicing is done
                if st.session_state.show_download_buttons:
                    self.show_download_buttons()

    def adjust_image_position(self, y_offset, grid_type):
        if st.session_state.processed_image:
            # Get stored dimensions
            canvas_height = st.session_state.canvas_height
            image_height = st.session_state.image_height
            
            # Create new background
            final_img = Image.new('RGB', (3112, canvas_height), st.session_state.bg_color)
            
            # Calculate paste position with bounds checking
            base_y = (canvas_height - image_height) // 2
            paste_y = base_y + y_offset
            
            # Ensure image stays within canvas bounds
            paste_y = max(canvas_height - image_height, min(0, paste_y))
            
            # Paste image at adjusted position
            final_img.paste(st.session_state.processed_image, (0, paste_y))
            st.session_state.final_image = final_img

    def process_image(self, uploaded_file, bg_color, grid_type):
        # Set canvas height based on grid type
        if grid_type == "1x3":
            canvas_height = 1350
        elif grid_type == "2x3":
            canvas_height = 2702
        else:  # 3x3
            canvas_height = 4054

        # Load and process image
        image = Image.open(uploaded_file)
        
        # Scale to width of 3112px while maintaining aspect ratio
        scale_ratio = 3112 / image.size[0]
        new_height = int(image.size[1] * scale_ratio)
        
        # Resize image
        resized_img = image.resize((3112, new_height), Image.Resampling.LANCZOS)
        
        # Store processed image and dimensions
        st.session_state.processed_image = resized_img
        st.session_state.image_height = new_height
        st.session_state.canvas_height = canvas_height
        
        # Calculate maximum offset to prevent background exposure
        max_offset = max(1, abs(new_height - canvas_height) // 2)  # Ensure at least 1px difference
        st.session_state.max_offset = max_offset
        
        # Create initial final image with proper height
        final_img = Image.new('RGB', (3112, canvas_height), bg_color)
        
        # Center the image vertically
        paste_y = (canvas_height - new_height) // 2
        final_img.paste(resized_img, (0, paste_y))
        
        # Store the final image
        st.session_state.final_image = final_img
        
        # Reset y_offset to 0
        st.session_state.y_offset = 0

    def add_guidelines(self, image):
        """Add yellow guidelines based on grid type"""
        from PIL import ImageDraw
        draw = ImageDraw.Draw(image)
        grid_type = st.session_state.get('grid_type', '1x3')
        
        # Calculate preview window thirds
        width = 3112  # Fixed width
        first_third_x = width // 3
        second_third_x = (width * 2) // 3
        
        if grid_type == "1x3":
            height = 1350
            # Add vertical guidelines
            draw.line([(first_third_x, 0), (first_third_x, height)], fill='yellow', width=2)
            draw.line([(second_third_x, 0), (second_third_x, height)], fill='yellow', width=2)
            
        elif grid_type == "2x3":
            height = 2702
            # Add vertical guidelines
            draw.line([(first_third_x, 0), (first_third_x, height)], fill='yellow', width=2)
            draw.line([(second_third_x, 0), (second_third_x, height)], fill='yellow', width=2)
            # Add horizontal guideline
            draw.line([(0, 1350), (width, 1350)], fill='yellow', width=2)
            
        else:  # 3x3
            height = 4054
            # Add vertical guidelines
            draw.line([(first_third_x, 0), (first_third_x, height)], fill='yellow', width=2)
            draw.line([(second_third_x, 0), (second_third_x, height)], fill='yellow', width=2)
            # Add horizontal guidelines
            draw.line([(0, 1350), (width, 1350)], fill='yellow', width=2)
            draw.line([(0, 2702), (width, 2702)], fill='yellow', width=2)
        
        return image.crop((0, 0, width, height))  # Crop to exact dimensions

    def show_download_buttons(self):
        """Separate method to handle download buttons display"""
        grid_type = st.session_state.get('grid_type', '1x3')
        slices = []
        
        # Horizontal slicing coordinates (same for all grid types)
        x_coords = [(0, 1080), (1016, 2096), (2032, 3112)]
        
        if grid_type == "1x3":
            for i, (x_start, x_end) in enumerate(x_coords):
                slice_img = st.session_state.final_image.crop((x_start, 0, x_end, 1350))
                slices.append((f'slice_{i+1}.png', slice_img))
        elif grid_type == "2x3":
            y_coords = [(0, 1350), (1352, 2702)]
            for row, (y_start, y_end) in enumerate(y_coords):
                for col, (x_start, x_end) in enumerate(x_coords):
                    slice_img = st.session_state.final_image.crop((x_start, y_start, x_end, y_end))
                    slices.append((f'slice_row{row+1}_col{col+1}.png', slice_img))
        else:  # 3x3
            y_coords = [(0, 1350), (1352, 2702), (2704, 4054)]
            for row, (y_start, y_end) in enumerate(y_coords):
                for col, (x_start, x_end) in enumerate(x_coords):
                    slice_img = st.session_state.final_image.crop((x_start, y_start, x_end, y_end))
                    slices.append((f'slice_row{row+1}_col{col+1}.png', slice_img))

        # Create zip file
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for filename, img in slices:
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                zip_file.writestr(filename, img_byte_arr)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Download section
        st.markdown("### Download Options")
        
        # Download All button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.download_button(
                label="📦 Download All as ZIP",
                data=zip_buffer.getvalue(),
                file_name=f'slices_{timestamp}.zip',
                mime="application/zip",
                use_container_width=True,
                key="download_all"
            )
        
        st.markdown("---")
        st.markdown("### Individual Slices")
        
        # Individual download buttons in rows of 3
        for i in range(0, len(slices), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(slices):
                    filename, img = slices[i + j]
                    with cols[j]:
                        buf = io.BytesIO()
                        img.save(buf, format='PNG')
                        byte_data = buf.getvalue()
                        
                        st.download_button(
                            label=f"📥 Slice {i + j + 1}",
                            data=byte_data,
                            file_name=filename,
                            mime="image/png",
                            use_container_width=True,
                            key=f"download_slice_{i + j}"
                        )

if __name__ == "__main__":
    app = StreamlitImageSlicer()
    app.create_ui() 