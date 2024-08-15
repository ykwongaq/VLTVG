dataset = "marinedet"
data_root = "/mnt/hdd/davidwong/data/VLTVG/data"
split_root = "/mnt/hdd/davidwong/data/VLTVG/split/data"

output_dir = "/mnt/hdd/davidwong/models/VLTVG/intra_class_val_unseen_no_negative"
# train_split = "inter_class_train_no_negative"
test_split = "intra_class_val_unseen_no_negative"

checkpoint = "/mnt/hdd/davidwong/models/VLTVG/marinedet_intra_class_train_no_negative/checkpoint_best_acc.pth"
batch_size_test = 16

# resume = "/mnt/hdd/davidwong/models/VLTVG/pretrained/VLTVG_R50_unc.pth"

checkpoint_best = True
batch_size = 32
epochs = 90
lr_drop = 60
freeze_epochs = 10
freeze_modules = ["backbone", "input_proj", "trans_encoder", "bert"]
load_weights_path = "/mnt/hdd/davidwong/models/VLTVG/pretrained/VLTVG_R50_unc.pth"

model_config = dict(
    decoder=dict(
        type="DecoderWithExtraEncoder",
        num_queries=1,
        query_dim=256,
        norm_dim=256,
        return_intermediate=True,
        num_layers=6,
        layer=dict(
            type="MultiStageDecoderLayer",
            d_model=256,
            dim_feedforward=2048,
            dropout=0.0,
            word_attn_args=dict(
                type="MultiheadAttention",
                embed_dim=256,
                num_heads=8,
                dropout=0.1,
            ),
            img_attn_args=dict(
                type="MultiheadAttention",
                embed_dim=256,
                num_heads=8,
                dropout=0.1,
            ),
            img_feat_chunk_num=2,
        ),
        num_extra_layers=1,
        extra_layer=dict(
            type="DiscriminativeFeatEncLayer",
            d_model=256,
            img_query_with_pos=False,
            img2text_attn_args=dict(
                type="MultiheadAttention", embed_dim=256, num_heads=8, dropout=0.1
            ),
            img2textcond_attn_args=dict(
                type="MultiheadAttention", embed_dim=256, num_heads=8, dropout=0.1
            ),
            img2img_attn_args=dict(
                type="MHAttentionRPE",
                d_model=256,
                h=8,
                dropout=0.1,
                pos_x_range=[-20, 20],
                pos_y_range=[-20, 20],
                pos_index_offset=20,
            ),
            vl_verify=dict(
                text_proj=dict(
                    input_dim=256, hidden_dim=256, output_dim=256, num_layers=1
                ),
                img_proj=dict(
                    input_dim=256, hidden_dim=256, output_dim=256, num_layers=1
                ),
                scale=1.0,
                sigma=0.5,
                pow=2.0,
            ),
        ),
    )
)
