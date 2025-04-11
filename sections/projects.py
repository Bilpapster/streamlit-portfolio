import streamlit as st
from annotated_text import annotated_text, parameters, annotation

def get_projects_section():
    parameters.SHOW_LABEL_SEPARATOR = True
    parameters.BORDER_RADIUS = "0.25rem"
    parameters.PADDING = "0.5rem"
    parameters.LABEL_SPACING = "0.5rem"
    PYTHON_COLOR_CODE = "#a17e00"
    SCALA_COLOR_CODE = "#d73937"
    JAVA_COLOR_CODE = "#f39a32"
    HADOOP_COLOR_CODE = "#0ca8fa"
    SPARK_COLOR_CODE = "#dc5b19"
    LATEX_COLOR_CODE = "#207f7f"

    st.header("Stream DaQ")
    stream_daq_logo, stream_daq_description = st.columns(2)
    with stream_daq_logo:
        st.image("assets/images/Stream DaQ logo.png")
    with stream_daq_description:
        st.markdown("Real-time quality monitoring for data streams. 60+ metrics to cherry-pick the ones that fit your use-case! Part of active research project at [Datalab](http://datalab.csd.auth.gr/).")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/stream-DaQ",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Python", "core", PYTHON_COLOR_CODE),
        "\t",
        ("Pathway", "stream processing", "#162ceb"),
        "\t",
        ("Redis", "stateful operations", "#D82C20"),
        "\t",
        ("PostgreSQL", "source/sink", "#356790"),
    )
    st.write("Skills:")
    annotated_text(
        annotation("data streaming", background='#121212', border='1px solid grey'),
        "\t",
        annotation("real-time processing", background='#121212', border='1px solid grey'),
        "\t",
        annotation("data quality", background='#121212', border='1px solid grey'),
        "\t",
        annotation("software engineering", background='#121212', border='1px solid grey'),
    )
    st.divider()

    st.header("Cluster them out!")
    cluster_them_out_logo, cluster_them_out_description = st.columns(2)
    with cluster_them_out_logo:
        st.image("assets/images/Cluster them out logo.png")
    with cluster_them_out_description:
        st.markdown(
            "Scalable outlier detection workflow for spatial 2-dimensional data, leveraging clustering techniques. Part of University project co-developed with my friend and bright colleague, [Lazaros](https://github.com/lazarosgogos).")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/cluster-them-out",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Scala", "core", SCALA_COLOR_CODE),
        "\t",
        ("R", "core", "#2366b5"),
        "\t",
        ("Apache Spark", "computing framework", SPARK_COLOR_CODE),
    )
    st.write("Skills:")
    annotated_text(
        annotation("data mining", background='#121212', border='1px solid grey'),
        "\t",
        annotation("outlier detection", background='#121212', border='1px solid grey'),
        "\t",
        annotation("k-means clustering", background='#121212', border='1px solid grey'),
        "\t",
        annotation("hierarchical clustering", background='#121212', border='1px solid grey'),
    )
    st.divider()

    st.header("Big Data playground")
    big_data_playground_logo, big_data_playground_description = st.columns(2)
    with big_data_playground_logo:
        st.image("assets/images/Big Data playground.png")
    with big_data_playground_description:
        st.markdown(
            "University project featuring various algorithms & techniques for processing large volumes of both structured and unstructured data, including multi-threading programming, parallelization & distribution. Co-developed with my esteemed colleague, [Christos](https://github.com/balaktsis). The project will be open-sourced on semester end (Feb 2025).")
        # todo: enable button when the project is open-sourced
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/big-data-playground",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Java", "core", JAVA_COLOR_CODE),
        "\t",
        ("Scala", "core", SCALA_COLOR_CODE),
        "\t",
        ("Apache Hadoop", "map-reduce", HADOOP_COLOR_CODE),
        "\t",
        ("Apache Spark", "distribution", SPARK_COLOR_CODE),
        "\t",
        ("LaTeX", "reporting", LATEX_COLOR_CODE),
    )
    st.write("Skills:")
    annotated_text(
        annotation("big data analytics", background='#121212', border='1px solid grey'),
        "\t",
        annotation("multi-threading", background='#121212', border='1px solid grey'),
        "\t",
        annotation("distributed processing", background='#121212', border='1px solid grey'),
        "\t",
        annotation("graph mining", background='#121212', border='1px solid grey'),
        "\t",
        annotation("software engineering", background='#121212', border='1px solid grey'),
    )
    st.divider()

    st.header("Neural Networks (NNs) playground")
    nns_playground_logo, nns_playground_description = st.columns(2)
    with nns_playground_logo:
        st.image("assets/images/NNs playground.png")
    with nns_playground_description:
        st.write(
            "University project featuring various Deep Learning algorithms & techniques mainly focusing on image data. Among others, the project addresses the novel and non-trivial task of developing an \"Adder Autoencoder\" which takes as input two image digits and constructs their sum as image, as shown in the thumbnail figure.")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/NNs-playground",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Python", "core", PYTHON_COLOR_CODE),
        "\t",
        ("Jupiter Notebook", "computing platform", "#ed7936"),
        "\t",
        ("scikit-learn", "ML algorithms", "#f39b45"),
        "\t",
        ("Keras", "DL algorithms", "#cb1818"),
    )
    st.write("Skills:")
    annotated_text(
        annotation("machine learning", background='#121212', border='1px solid grey'),
        "\t",
        annotation("deep learning", background='#121212', border='1px solid grey'),
        "\t",
        annotation("multiclass image classification", background='#121212', border='1px solid grey'),
        "\t",
        annotation("image reconstruction", background='#121212', border='1px solid grey'),
    )
    st.divider()

    import base64
    st.header("SimpleSim")
    cluster_them_out_logo, cluster_them_out_description = st.columns(2)
    with cluster_them_out_logo:
        file_ = open("assets/images/SimpleSim animation.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
    with cluster_them_out_description:
        st.write(
            "A UAV and a ground target moving around in 3D space. All in one place, built from scratch and visualized! ")
        st.link_button("See source code",
                       url="https://github.com/Bilpapster/SimpleSim",
                       icon=":material/terminal:")
    st.write("Powered by:")
    annotated_text(
        ("Python", "core", PYTHON_COLOR_CODE),
        "\t",
        ("Matplotlib", "3D visualizations", "#d6854f"),
    )
    st.write("Skills:")
    annotated_text(
        annotation("software engineering", background='#121212', border='1px solid grey'),
        "\t",
        annotation("visualizations", background='#121212', border='1px solid grey'),
        "\t",
    )
    st.divider()

    st.write("It seems you have reached the end of this page! Luckily, my projects do not end here! Should you wish to see more, feel free to visit my GitHub profile, where 12+ past and current projects of mine have been made publicly available.")
    st.link_button("See GitHub profile",
                   url="https://github.com/Bilpapster/SimpleSim",
                   icon=":material/terminal:")


