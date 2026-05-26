import streamlit as st

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="مفكرتي الذكية", page_icon="📝", layout="centered")

# عنوان التطبيق بشكل أنيق
st.markdown("<h1 style='text-align: center; color: #4F46E5;'>📝 مفكرتي الذكية لإدارة المهام</h1>", unsafe_allow_html=True)
st.write("---")

# ميزة سحرية في ستريمليت لحفظ القائمة في الذاكرة حتى لا تختفي عند تحديث الصفحة
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# قسم إضافة مهمة جديدة
st.subheader("➕ إضافة مهمة جديدة")
col1, col2 = st.columns([4, 1]) # تقسيم السطر إلى عمودين (واحد للكتابة والآخر للزر)

with col1:
    new_task = st.text_input("بماذا تخططين اليوم؟", placeholder="اكتبي مهمتكِ هنا...", label_visibility="collapsed")

with col2:
    add_button = st.button("إضافة", use_container_width=True)

# إذا ضغطتِ على زر الإضافة وكان الحقل غير فارغ
if add_button and new_task:
    # حفظ المهمة كقاموس يحتوي على النص وحالة الإنجاز
    st.session_state.tasks.append({"text": new_task, "done": False})
    st.rerun() # إعادة تحديث الشاشة لتظهر المهمة فوراً

st.write("")

# قسم عرض المهام وإدارتها
st.subheader("📋 قائمة مهامكِ الحالية")

if not st.session_state.tasks:
    st.info("قائمتكِ فارغة حالياً! ابدئي بإضافة بعض المهام لتنظيم يومكِ. ✨")
else:
    # عرض كل مهمة في سطر منفصل مع مربع اختيار ورص حذف
    for index, task in enumerate(st.session_state.tasks):
        col_check, col_text, col_del = st.columns([1, 5, 1])
        
        with col_check:
            # مربع اختيار لتحديد ما إذا تمت المهمة أم لا
            is_done = st.checkbox("", value=task["done"], key=f"check_{index}")
            if is_done != task["done"]:
                st.session_state.tasks[index]["done"] = is_done
                st.rerun()
                
        with col_text:
            # إذا كانت المهمة منجزة، نعرضها بخط مائل وباهت، وإلا نعرضها بشكل عادي
            if task["done"]:
                st.markdown(f"<p style='text-decoration: line-through; color: gray;'>{task['text']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='font-size: 18px;'><b>{task['text']}</b></p>", unsafe_allow_html=True)
                
        with col_del:
            # زر حذف المهمة
            if st.button("❌", key=f"del_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()

# زر لمسح كافة المهام المنجزة دفعة واحدة لتنظيف القائمة
st.write("---")
if st.button("🧹 تنظيف المهام المنجزة"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.rerun()
