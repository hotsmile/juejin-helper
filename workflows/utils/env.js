const env = process.env || {};

module.exports = {
  /* 掘金Cookie */
  // COOKIE: env.COOKIE,
  COOKIE: "__tea_cookie_tokens_2608=%7B%22web_id%22%3A%227435802743686596096%22%2C%22user_unique_id%22%3A%227435802743686596096%22%2C%22timestamp%22%3A1731282775939%7D; store-region=cn-fj; store-region-src=uid; _ga=GA1.2.1234608364.1731282805; _tea_utm_cache_2018={\"utm_source\":\"gold_browser_extension\"}; _tea_utm_cache_576092={\"utm_source\":\"gold_browser_extension\"}; _tea_utm_cache_2608={\"utm_source\":\"gold_browser_extension\"}; passport_csrf_token=0f056c92213acda61f390cf516b433eb; passport_csrf_token_default=0f056c92213acda61f390cf516b433eb; n_mh=tzO9uUFHV3SORYqaaDIX3-5k3wt2U651nnC_0LtXeDg; sid_guard=1e7a87f55b41624e18532aa4906393f5|1762929397|31536000|Thu,+12-Nov-2026+06:36:37+GMT; uid_tt=969de5016bd00e1d709cb4b041d86546; uid_tt_ss=969de5016bd00e1d709cb4b041d86546; sid_tt=1e7a87f55b41624e18532aa4906393f5; sessionid=1e7a87f55b41624e18532aa4906393f5; sessionid_ss=1e7a87f55b41624e18532aa4906393f5; is_staff_user=false; sid_ucp_v1=1.0.0-KDU5ZWE3N2NkZmIzODRiYjZjZTk0N2E5MTA4NjY1ZjRhMjg1NGIzNjIKFgjorMC-_fXBBxD11dDIBhiwFDgIQDgaAmxmIiAxZTdhODdmNTViNDE2MjRlMTg1MzJhYTQ5MDYzOTNmNQ; ssid_ucp_v1=1.0.0-KDU5ZWE3N2NkZmIzODRiYjZjZTk0N2E5MTA4NjY1ZjRhMjg1NGIzNjIKFgjorMC-_fXBBxD11dDIBhiwFDgIQDgaAmxmIiAxZTdhODdmNTViNDE2MjRlMTg1MzJhYTQ5MDYzOTNmNQ; session_tlb_tag=sttt|20|HnqH9VtBYk4YUyqkkGOT9f_________oL0sKvNBD8BjQSk20bR4RP8aPKk6cxvT9KgFzgIh5RMk=; session_tlb_tag_bk=sttt|20|HnqH9VtBYk4YUyqkkGOT9f_________oL0sKvNBD8BjQSk20bR4RP8aPKk6cxvT9KgFzgIh5RMk=; _ga_S695FMNGPJ=GS2.2.s1762929398$o2$g0$t1762929398$j60$l0$h0; csrf_session_id=a63e571a03d7917372857e2113e40cc1",

  /* 多用户掘金Cookie, 当有1名以上用户时填写, 支持同时最多可配置5名用户 */
  COOKIE_2: env.COOKIE_2,
  COOKIE_3: env.COOKIE_3,
  COOKIE_4: env.COOKIE_4,
  COOKIE_5: env.COOKIE_5,
  /**
   * 邮箱配置
   * user 发件人邮箱, pass, 发件人密码, to收件人
   */
  EMAIL_USER: env.EMAIL_USER,
  EMAIL_PASS: env.EMAIL_PASS,
  EMAIL_TO: env.EMAIL_TO,
  /**
   * 钉钉配置
   * https://open.dingtalk.com/document/robots/custom-robot-access
   */
  DINGDING_WEBHOOK: env.DINGDING_WEBHOOK,
  /**
   * PushPlus配置
   * http://www.pushplus.plus/doc/guide/openApi.html
   */
  PUSHPLUS_TOKEN: env.PUSHPLUS_TOKEN,
  /**
   * 企业微信机器人配置
   * https://developer.work.weixin.qq.com/document/path/91770
   */
  WEIXIN_WEBHOOK: env.WEIXIN_WEBHOOK,
  /**
   * server酱推送key
   * https://sct.ftqq.com/sendkey
   */
  SERVERPUSHKEY: env.SERVERPUSHKEY,
  /**
   * 飞书配置
   */
  FEISHU_WEBHOOK: env.FEISHU_WEBHOOK
};
